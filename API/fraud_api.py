from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import json
import os

app = FastAPI(title="Real-Time Fraud Detection API")

# Define request schema
class Transaction(BaseModel):
    transaction_amount: float
    transactions_last_24h: int
    failed_logins_24h: int
    is_foreign_transaction: int
    is_new_device: int
    is_new_location: int


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "Modeling Data", "fraud_detection_xgb_model.pkl")
feature_path = os.path.join(BASE_DIR, "Modeling Data", "model_features.json")

model = joblib.load(model_path)

with open(feature_path) as f:
    model_features = json.load(f)


@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}


@app.post("/predict")
def predict(transaction: Transaction):

    df = pd.DataFrame([transaction.dict()])

    df = pd.get_dummies(df)

    df = df.reindex(columns=model_features, fill_value=0)

    fraud_prob = model.predict_proba(df)[0][1]

    fraud_pred = int(fraud_prob > 0.8)

    return {
        "fraud_prediction": fraud_pred,
        "fraud_probability": float(fraud_prob),
        "alert": "Fraud Detected" if fraud_pred else "Normal Transaction"
    }