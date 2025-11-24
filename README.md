# 💳 Credit Card Monthly Statement Analyzer  
**Python Automation | Finance | Spending Behavior Analysis**

This project analyzes monthly credit card spending across categories such as Food, Travel, Shopping, and Bills.  
It calculates total spending, evaluates financial behavior, classifies spending levels, and generates risk warnings — very similar to what banking analysts and credit risk teams do.

It’s a realistic beginner-to-intermediate Python project focused on **financial analytics** and **behavioral risk detection**.

---

## 📌 Features

- Processes monthly credit card spendings
- Calculates:
  - Total spending per month
  - Spending-to-credit-limit ratio
- Classifies spending behavior:
  - **High Spender**
  - **Moderate Spender**
  - **Low Spender**
- Detects risk signals:
  - Large category spikes
  - Impulsive shopping behavior
  - High fixed costs
- Produces clean monthly reports with warnings

---

## 🛠️ Tech Stack

- **Python 3**
- Dictionaries
- Loops
- Conditional Logic
- Financial ratio analysis

---

## 🧮 How the Data Works

### Input dictionary structure:

```python
credit_card = {
    'Name': 'Abbas',
    'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],

    'Spendings': [
        {'Food':200,'Travel':50,'Shopping':150,'Bills':120},
        {'Food':180,'Travel':30,'Shopping':80,'Bills':130},
        {'Food':250,'Travel':100,'Shopping':200,'Bills':140},
        {'Food':300,'Travel':20,'Shopping':90,'Bills':110},
        {'Food':150,'Travel':80,'Shopping':250,'Bills':130}
    ],

    'Credit Limit': 1500
}
```
Each Spendings[i] dictionary represents the spending categories for month Months[i].


```yaml
📊 Sample Output

--- Report for month Jan ---
Total Spending: 520
Status Ratio: 0.35
Warnings:
- High Food Priority

--- Report for month Mar ---
Total Spending: 690
Status Ratio: 0.46
Warnings:
- Large Category Spend detected
- Impulsive shopping behaviour

```


Warnings reflect real financial red flags such as:
unusually high category expenses
fixed cost pressure
impulsive shopping pattern


▶️ How to Run

Clone the repository:

```python
git clone https://github.com/abbashumbatov/Credit_Card_Statement_Analyzer.git
cd Credit_Card_Statement_Analyzer
```

Run the script:

```python
python main.py
```


## 👤 Author
## Abbas Humbatov
## https://www.linkedin.com/in/abbas-humbatov-/






