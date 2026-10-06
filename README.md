# 📉 Customer Churn Predictor

A beginner-friendly Machine Learning project that predicts whether a customer is likely to **Churn** or **Stay** using a **Decision Tree Classifier**.

The model uses customer information such as:

- Age
- Tenure
- Monthly Charges
- Support Tickets

This project is part of my Python → Data Science → Machine Learning learning journey.

---

## 🚀 Project Overview

Customer churn means a customer stops using a company's product or service.

This project uses Machine Learning to classify customers into two categories:

```text
CHURN
STAY
```

The project demonstrates a complete basic classification workflow:

```text
Customer Dataset
       ↓
Feature Selection
       ↓
Train/Test Split
       ↓
Decision Tree Classifier
       ↓
Model Training
       ↓
Accuracy Evaluation
       ↓
New Customer Input
       ↓
CHURN / STAY Prediction
```

---

## 🎯 Objective

The main objective of this project is to understand how a **Decision Tree Classifier** works in a Machine Learning classification problem.

The project demonstrates:

- Feature selection
- Target selection
- Train/test splitting
- Decision Tree classification
- Model training
- Model prediction
- Accuracy evaluation
- Controlling tree complexity with `max_depth`
- Predicting results for new customers

---

## 🧠 Machine Learning Concepts

### 1. Features

The model uses four customer features:

```text
Age
Tenure
MonthlyCharges
SupportTickets
```

These features provide information about the customer.

In Machine Learning:

```text
X → Input Features
```

---

### 2. Target

The target column is:

```text
Churn
```

The values are:

```text
0 → Customer stays
1 → Customer churns
```

The model learns the relationship between customer information and churn behavior.

---

## 🌳 Decision Tree Classifier

This project uses:

```python
DecisionTreeClassifier()
```

A Decision Tree makes predictions by learning a series of decision rules from the training data.

Conceptually, the model may learn rules similar to:

```text
Is tenure low?
      ↓
   YES
      ↓
Are support tickets high?
      ↓
   YES
      ↓
   CHURN
```

These rules are **not manually created**.

The Decision Tree learns useful splits automatically from the training dataset.

---

## 📏 Controlling Tree Depth

The model uses:

```python
max_depth=5
```

`max_depth` controls how deep the Decision Tree is allowed to grow.

A very deep tree can become overly complex and may memorize the training data.

This can lead to:

```text
Overfitting
```

Limiting the depth helps keep the model simpler.

---

## 🔀 Train/Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

Training data is used to teach the model.

Testing data is used to evaluate how well the model performs on unseen data.

The project uses:

```python
random_state=42
```

to make the split reproducible.

---

## 📈 Model Evaluation

The project uses **Accuracy** to evaluate the classifier.

Accuracy represents the percentage of predictions that were correct.

Example:

```text
Accuracy: 83.33%
```

This means the model correctly classified approximately 83% of the test samples in that particular train/test split.

> **Note:** The dataset contains only 30 records, so the accuracy should not be interpreted as a reliable real-world churn prediction performance.

---

## 📊 Dataset

The project uses a sample dataset containing 30 customers.

Example:

```csv
CustomerID,Age,Tenure,MonthlyCharges,SupportTickets,Churn
C001,22,2,850,5,1
C002,35,24,650,1,0
C003,28,4,920,6,1
C004,42,36,550,0,0
C005,25,3,780,4,1
```

### Dataset Columns

| Column | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Age | Customer age |
| Tenure | Number of months with the service |
| MonthlyCharges | Customer's monthly charges |
| SupportTickets | Number of support tickets |
| Churn | Target: 0 = Stay, 1 = Churn |

`CustomerID` is not used as a model feature because it is only an identifier and does not provide meaningful predictive information.

---

## 🧪 Example Prediction

The program asks for new customer information:

```text
===== ENTER CUSTOMER DETAILS =====

Age: 22
Tenure (months): 9
Monthly charges: ₹999
Support tickets: 5
```

The trained model then predicts:

```text
===== CUSTOMER CHURN PREDICTION =====

Age              : 22
Tenure           : 9 months
Monthly Charges  : ₹999.0
Support Tickets  : 5
Predicted Result : CHURN
```

---

## 🗂️ Project Structure

```text
python-customer-churn-predictor/
│
├── main.py
├── churn_predictor.py
├── customers.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsible for:

- Creating the predictor
- Training the model
- Taking customer information
- Calling the prediction method

### `churn_predictor.py`

Contains the Machine Learning logic:

- Loading the dataset
- Preparing features and target
- Splitting the dataset
- Creating the Decision Tree
- Training the model
- Evaluating accuracy
- Predicting churn for new customers

### `customers.csv`

Contains the customer training dataset.

### `requirements.txt`

Contains the required Python libraries.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ayushman-ece/python-customer-churn-predictor.git
```

Move into the project directory:

```bash
cd python-customer-churn-predictor
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run:

```bash
python main.py
```

The model will first train and display its accuracy.

Then it will ask for customer information.

Example:

```text
Age: 24
Tenure (months): 3
Monthly charges: 900
Support tickets: 6
```

The program will return:

```text
Predicted Result : CHURN
```

---

## 🧰 Technologies Used

- Python
- Pandas
- Scikit-learn
- Decision Tree
- Machine Learning
- Classification
- CSV

---

## 📦 Requirements

The project requires:

```text
pandas
scikit-learn
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📚 What I Learned

Through this project, I learned:

1. What customer churn means
2. How to select meaningful features
3. How to select a target variable
4. How to split data into training and testing sets
5. How Decision Tree classification works
6. How a model learns decision rules from data
7. How `max_depth` controls tree complexity
8. Why overly complex trees can overfit
9. How to train a classification model
10. How to evaluate a classifier using accuracy
11. How to use a trained model to predict new customers

---

## 🔄 Classification Models So Far

This project follows my previous Machine Learning projects.

### Project #50 — Linear Regression

```text
Employee Information
        ↓
Linear Regression
        ↓
Salary: ₹65,000
```

Used for predicting a numerical value.

### Project #51 — Logistic Regression

```text
Student Information
        ↓
Logistic Regression
        ↓
PASS / FAIL
```

Used for classification.

### Project #52 — Decision Tree

```text
Customer Information
        ↓
Decision Tree
        ↓
CHURN / STAY
```

This project introduces tree-based Machine Learning.

---

## ⚠️ Limitations

This project is designed for learning purposes.

Limitations include:

- Only 30 customer records are used.
- The dataset is synthetic/sample data.
- Real customer churn depends on many more factors.
- Accuracy can vary depending on the train/test split.
- The model has not been validated on a large real-world dataset.
- The current application has basic input validation.

Therefore, this model should **not be used for real business decisions** without a much larger and properly validated dataset.

---

## 🔮 Future Improvements

Possible improvements include:

- Use a larger real-world dataset
- Add more customer behavior features
- Add contract type
- Add payment method
- Add customer satisfaction
- Add service usage information
- Add confusion matrix
- Add precision, recall, and F1-score
- Compare Decision Tree with Random Forest
- Tune hyperparameters
- Perform cross-validation
- Add data visualization
- Build a Streamlit web application
- Deploy the model as an API

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece

---

## 🛣️ Learning Journey

This project is part of my long-term journey:

```text
Python
   ↓
Data Analysis
   ↓
Data Science
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
LLMs
   ↓
RAG
   ↓
Agentic AI
```

The goal is to build practical projects while understanding the concepts behind them step-by-step.