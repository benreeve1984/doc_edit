import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from pydantic import BaseModel, Field
from typing import Optional, List
from difflib import SequenceMatcher

# 1. Create a Flask app instance
app = Flask(__name__)

# 2. Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "YOUR_API_KEY_HERE"))

# 3. Define the response schema using Pydantic
class TextTransformation(BaseModel):
    edited_text: str
    explanation: Optional[str] = Field(default=None)
    style_changes: List[str] = Field(default_factory=list)

# 4. Define the style guide prompt
STYLE_GUIDE_PROMPT = """You are a professional stylistic editor with deep industry expertise in Mortgage Capital Requirements. 
Transform the text according to these guidelines:

1. Use UK English (e.g., "organisation" not "organization")
2. Write in clear, neutral, objective tone without first-person pronouns
3. Use active voice unless passive is clearly more appropriate
4. Keep language direct and straightforward
5. Use past tense as main tense
6. Avoid hedging words ("suggest," "perhaps," "possibly")
7. Format numbers: spell out 0-9, numerals for 10+, "m" for million, "bn" for billion
8. Structure into well-organized paragraphs
9. Keep sentences to maximum 20 words
10. Maintain all technical terms, formulas, and acronyms exactly as provided

Provide the edited text along with a list of specific changes made."""

# 4. Home route to serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# 5. API endpoint to transform selected text
@app.route("/transform", methods=["POST"])
def transform_text():
    """Handle text transformation requests with custom instructions or style guide."""
    data = request.get_json()
    selected_text = data.get("text")
    instruction = data.get("instruction")
    use_style_guide = data.get("use_style_guide", False)

    if not selected_text:
        return jsonify({"error": "Missing text"}), 400
    
    if not instruction and not use_style_guide:
        return jsonify({"error": "Missing instruction"}), 400

    try:
        # Prepare the system message based on whether we're using the style guide
        system_message = STYLE_GUIDE_PROMPT if use_style_guide else (
            "You are a writing assistant that transforms text according to user instructions. "
            "Preserve the text's structure while editing."
        )

        # Prepare the user message
        user_message = (
            f"Please transform the following text according to the style guide:\n{selected_text}"
            if use_style_guide else
            f"Please {instruction} the following text:\n{selected_text}"
        )

        # Call GPT with structured output using parse method
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            response_format=TextTransformation,
        )

        # Get the transformed text
        result = completion.choices[0].message.parsed
        
        # Calculate character-level differences
        matcher = SequenceMatcher(None, selected_text, result.edited_text)
        diff_indices = []
        
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in ('replace', 'insert'):
                # Track changed or inserted characters
                for idx in range(j1, j2):
                    diff_indices.append({"index": idx, "type": tag})
        
        # Create response dictionary with both the parsed result and diff indices
        response_data = {
            "edited_text": result.edited_text,
            "explanation": result.explanation,
            "style_changes": result.style_changes,
            "diff_indices": diff_indices
        }
        
        return jsonify(response_data)

    except Exception as e:
        app.logger.error(f"Error in transform_text: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)