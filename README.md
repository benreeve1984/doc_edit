# Model Document Auto-Editor

A Flask-based web application that helps users edit and transform markdown documents according to style guidelines or custom instructions. The application leverages OpenAI's GPT models to provide intelligent text transformations while maintaining document structure.

## Features

- **Markdown Editor**: Built-in markdown editor with preview functionality
- **File Operations**: Load and save markdown files
- **Text Transformation**:
  - Apply predefined style guide rules
  - Use custom transformation instructions
  - Highlight changes in real-time
- **Change Management**: Accept or reject transformations
- **UK English Style Guide**: Specialized for Mortgage Capital Requirements documentation

## Prerequisites

- Python 3.8+
- OpenAI API key
- Flask and its dependencies

## Installation

1. Clone the repository and navigate to the project directory
2. Create and activate a virtual environment
3. Install dependencies from requirements.txt
4. Set up your OpenAI API key as an environment variable

## Usage

1. Start the Flask application by running app.py
2. Open your browser and navigate to http://localhost:5000
3. Use the interface to:
   - Load markdown files
   - Select text for transformation
   - Apply style guide or custom transformations
   - Review and accept/reject changes
   - Save modified documents

## Style Guide Rules

The application enforces the following style guidelines:

1. UK English spelling and conventions
2. Clear, neutral, objective tone
3. Active voice preference
4. Direct and straightforward language
5. Past tense as main tense
6. Minimal hedging words
7. Standardized number formatting
8. Well-organized paragraph structure
9. Concise sentences (max 20 words)
10. Preservation of technical terms and formulas

## Project Structure

The project contains the following key files:
- app.py: Flask application main file
- templates/index.html: Web interface template
- static/styles/: CSS stylesheets
- README.md: Project documentation
- requirements.txt: Python dependencies

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Error Handling

The application includes comprehensive error handling for:
- File operations
- API communication
- Text transformations
- Invalid inputs

## Security Considerations

- API keys are managed through environment variables
- Input validation is implemented for all user inputs
- CSRF protection is enabled by default

## License

MIT License

## Contributing

Contributions are welcome! Please read our Contributing Guidelines for details on submitting pull requests.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. 