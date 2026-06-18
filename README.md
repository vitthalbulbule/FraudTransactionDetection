# AI Fraud Detection System

## Project Overview

The AI Fraud Detection System is a Machine Learning-based web application that detects fraudulent financial transactions. The model analyzes transaction details and predicts whether a transaction is legitimate or fraudulent.

The application is built using Flask for the backend and Random Forest Classifier for fraud prediction.

---

## Dataset Information

- Dataset Name: PaySim Financial Transactions Dataset
- Total Transactions: 6,362,620
- Legitimate Transactions: 6,354,407
- Fraudulent Transactions: 8,213

### Features Used

- type
- amount
- oldbalanceOrg
- newbalanceOrig
- oldbalanceDest
- newbalanceDest
- orig_type
- dest_type

---

## Data Preprocessing

The following preprocessing techniques were applied:

- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- Pipeline implementation using Scikit-Learn

---

## Machine Learning Model

**Algorithm:** Random Forest Classifier

The complete preprocessing pipeline and model were saved using Joblib and deployed through Flask.

---

## Model Performance

| Metric | Score |
|----------|----------|
| Accuracy | 99.97% |
| Precision | 96% |
| Recall | 79% |
| F1-Score | 87% |

### Confusion Matrix

```text
[[1270855      49]
 [    337    1283]]
```

Where:

- True Negatives (TN): 1,270,855
- False Positives (FP): 49
- False Negatives (FN): 337
- True Positives (TP): 1,283

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- Bootstrap
- Joblib

---

## Project Structure

```text
FraudDetection/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

---

## Application Features

- Fraud Detection Prediction
- Fraud Probability Score
- User-Friendly Dashboard
- Real-Time Transaction Analysis
- Machine Learning Powered Decision Making

---

## Future Enhancements

- XGBoost Implementation
- Interactive Analytics Dashboard
- Cloud Deployment
- Real-Time Banking Integration
- API-Based Prediction Service

---

## Author

Vitthal Bulbule

AI & Data Science Engineering Student
