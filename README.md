# 🚀 Fraud Detection System using XGBoost + MLP (Ensemble Learning)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost%20%7C%20SMOTE-orange)
![Status](https://img.shields.io/badge/Project-Completed-green)
![Type](https://img.shields.io/badge/Project-Academic-lightgrey)

---

## 📌 Deskripsi Project

Project ini merupakan sistem **deteksi fraud transaksi keuangan** berbasis Machine Learning menggunakan pendekatan **ensemble learning dan feature engineering**.

Sistem ini mampu menganalisis transaksi dan mengklasifikasikan apakah transaksi tersebut:
- ✔ Normal Transaction
- ⚠ Fraud Transaction

Model utama yang digunakan:
- 🌳 **XGBoost Classifier** (model utama)
- 🧠 **MLP Neural Network** (pendukung konsep ensemble)
- ⚖️ **SMOTE** untuk balancing dataset

---

## 🎯 Tujuan Project

- Mendeteksi transaksi fraud secara otomatis
- Mengurangi false transaction dalam sistem keuangan
- Meningkatkan performa model dengan feature engineering
- Menyediakan API dan dashboard untuk simulasi real-time

---

## 🧠 Cara Kerja Sistem

### 1. Data Collection
Dataset transaksi keuangan dikumpulkan dari file CSV.

### 2. Data Cleaning
- Handling missing values
- Drop duplicate data
- Convert datetime format

### 3. Feature Engineering
Menambahkan fitur penting:
- amount_ratio
- txn_per_day
- account_trust_score
- device_risk
- night_transaction

### 4. Balancing Data
Menggunakan **SMOTE** untuk mengatasi imbalance fraud vs non-fraud.

### 5. Model Training
- XGBoost Classifier
- Hyperparameter tuning (GridSearchCV)
- Stratified K-Fold Cross Validation

### 6. Evaluation
Evaluasi model menggunakan:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

### 7. Deployment
- Flask / FastAPI backend
- Streamlit dashboard
- Real-time prediction API

---

## 🧠 Teknologi yang Digunakan

- Python 3.10
- Pandas & NumPy
- Scikit-Learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Matplotlib & Seaborn
- Joblib
- FastAPI / Streamlit

---

## 📂 Struktur Project
