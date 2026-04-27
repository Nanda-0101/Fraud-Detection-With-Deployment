import streamlit as st
import requests
import pandas as pd

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("Real-Time Fraud Detection System")

st.markdown("Simulate a transaction and check fraud risk using the deployed ML model.")

st.divider()

# Transaction Input
st.subheader("Transaction Details")
col1, col2, col3 = st.columns(3)

with col1:
    transaction_amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )

with col2:
    transactions_last_24h = st.number_input(
        "Transactions Last 24h",
        min_value=0,
        value=1
    )

with col3:
    failed_logins_24h = st.number_input(
        "Failed Logins (24h)",
        min_value=0,
        value=0
    )

col4, col5, col6 = st.columns(3)

with col4:
    is_foreign_transaction = st.selectbox("Foreign Transaction", [0, 1])

with col5:
    is_new_device = st.selectbox("New Device", [0, 1])

with col6:
    is_new_location = st.selectbox("New Location", [0, 1])

st.divider()

# Predict Button
if st.button("Check Fraud Risk"):

    payload = {
        "transaction_amount": transaction_amount,
        "transactions_last_24h": transactions_last_24h,
        "failed_logins_24h": failed_logins_24h,
        "is_foreign_transaction": is_foreign_transaction,
        "is_new_device": is_new_device,
        "is_new_location": is_new_location
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:

        result = response.json()

        st.subheader("Prediction Result")

        fraud_prob = result["fraud_probability"]
        fraud_pred = result["fraud_prediction"]

        colA, colB = st.columns(2)

        with colA:
            st.metric("Fraud Probability", f"{fraud_prob:.2f}")

        with colB:
            st.metric("Prediction", "Fraud" if fraud_pred else "Normal")

        if fraud_pred == 1:
            st.error("Fraud Detected!")
        else:
            st.success("Transaction Normal")

    else:
        st.error("API connection failed")