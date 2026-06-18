from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("fraud_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = pd.DataFrame({
        'type':[request.form['type']],
        'amount':[float(request.form['amount'])],
        'oldbalanceOrg':[float(request.form['oldbalanceOrg'])],
        'newbalanceOrig':[float(request.form['newbalanceOrig'])],
        'oldbalanceDest':[float(request.form['oldbalanceDest'])],
        'newbalanceDest':[float(request.form['newbalanceDest'])],
        'orig_type':[request.form['orig_type']],
        'dest_type':[request.form['dest_type']]
    })

    prediction = model.predict(data)[0]

    probability = round(
        model.predict_proba(data)[0][1] * 100,
        2
    )

    result = "Fraud Transaction" if prediction == 1 else "Legitimate Transaction"

    return render_template(
        "index.html",
        prediction=result,
        probability=probability
    )

if __name__ == "__main__":
    app.run(debug=True)