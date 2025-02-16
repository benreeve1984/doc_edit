## Variable Selection Using Single Factor Analysis

For making PD model, choosing right variable is very important because good variable make prediction better. In this model, we use **single factor analysis** for checking which variable is useful for predicting default. **Single factor analysis** is simple method where we check one variable at a time to see how much it affect customer default.

### **Step 1: Collecting Candidate Variables**

First, we take many variable from bank data. These variable come from different source like loan application, credit history, and transaction data. Some common variable we check include:

- **Income** (higher income may have less default)
- **Loan Amount** (big loan compare to income may have more risk)
- **Loan-to-Value (LTV) Ratio** (higher LTV mean more chance of default)
- **Credit History** (bad credit history mean high risk)
- **Employment Status** (unemployed person may not pay loan)
- **Age** (younger or older people may have different risk)
- **Past Loan Behavior** (if past loan paid on time, risk is lower)

These are just example, real model check many more variable.

### **Step 2: Analyzing Each Variable Separately**

Once we collect all possible variable, we check each one **separately** to see how much it affect default. For this, we divide data into different **groups** based on value of variable and compare default rate.

#### **Example: Income Analysis**
If we take **income**, we divide customer into different income range like this:

| Income Range   | Default Rate |
|---------------|-------------|
| Below $20,000 | 12%         |
| $20,000-$50,000 | 7%        |
| Above $50,000 | 3%          |

From this, we see that **lower income customers** have **higher default rate**. This means income is useful variable for model.

#### **Example: Credit History Analysis**
For **credit history**, we check default rate based on past payment behavior:

| Credit Score Range | Default Rate |
|--------------------|-------------|
| Below 600         | 15%         |
| 600-700           | 8%          |
| Above 700         | 2%          |

This show **people with bad credit score default more**, so credit score is good variable.

### **Step 3: Removing Weak and Redundant Variables**

Some variable may not be good for model. We remove variables that have:

- **No clear pattern with default** (for example, if customer age is random and not affect default, we remove it)
- **Too many missing values** (if a variable has too many missing numbers, it is not reliable)
- **Similar meaning as another variable** (for example, "loan amount" and "loan-to-income ratio" may tell same thing, so we keep only one)

### **Step 4: Selecting Final Variables for Model**

After analyzing all variables, we select only the **most useful** variables for model. This help in making model:

1. **More accurate** – Model focus on strong variables, reducing noise.
2. **Easier to interpret** – Simpler model is better for business and regulation.
3. **More stable over time** – Good variables work well even when economy change.

Good variable selection is very important because too many bad variable can make model confuse and reduce accuracy. Also, regulator like **Basel rule** say model should be **simple and understandable**, so single factor analysis help in making model good for both business and compliance.