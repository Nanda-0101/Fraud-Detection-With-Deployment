# Real-Time Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange)

Sistem deteksi penipuan transaksi keuangan berbasis Machine Learning menggunakan **XGBoost**, dilengkapi dengan REST API (FastAPI), simulasi streaming transaksi, dan dashboard interaktif (Streamlit).

---

## Cara Kerja Sistem

### 1. Eksplorasi & Preprocessing Data (`EDA_Preprocessing.ipynb`)

- Memuat dataset transaksi dari `Fraud detection Dataset.csv`
- Menghapus duplikat dan mengkonversi kolom waktu ke format datetime
- Mengisi nilai kosong: numerik dengan **median**, kategorik dengan **modus**
- Visualisasi distribusi fitur, analisis fraud vs non-fraud, dan heatmap korelasi
- Menyimpan data bersih ke `df_clean.csv`

### 2. Feature Engineering & Training Model (`Feature_Engineering.ipynb`)

**Fitur yang dibuat:**
| Fitur | Deskripsi |
|---|---|
| `amount_ratio` | Rasio transaksi saat ini terhadap rata-rata transaksi |
| `txn_per_day` | Intensitas transaksi per hari |
| `account_trust_score` | Skor kepercayaan akun berdasarkan usia & gagal login |
| `device_risk` | Skor risiko perangkat (device baru + lokasi baru + transaksi asing) |
| `night_transaction` | Flag transaksi tengah malam (jam 00.00–05.00) |
| `txn_hour`, `txn_day`, `txn_month`, `is_weekend` | Fitur berbasis waktu |

**Proses pelatihan:**
1. Split data: 80% train, 20% test (stratified)
2. Oversampling dengan **SMOTE** untuk menangani ketidakseimbangan kelas
3. Tuning hyperparameter dengan **GridSearchCV + StratifiedKFold (5-fold)**
4. Melatih **XGBoostClassifier** dengan parameter terbaik
5. Evaluasi: Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix
6. Menyimpan model ke `fraud_detection_xgb_model.pkl`

### 3. REST API (`api.py`)

API dibangun dengan **FastAPI** dan menerima data transaksi secara real-time.

**Endpoint:**
- `GET /` — Status API
- `POST /predict` — Prediksi fraud untuk satu transaksi

**Contoh Request:**
```json
{
  "transaction_amount": 5000.0,
  "transactions_last_24h": 10,
  "failed_logins_24h": 3,
  "is_foreign_transaction": 1,
  "is_new_device": 1,
  "is_new_location": 0
}
```

**Contoh Response:**
```json
{
  "fraud_prediction": 1,
  "fraud_probability": 0.92,
  "alert": "Fraud Detected"
}
```

> Transaksi diklasifikasikan sebagai **fraud** jika probabilitas > 0.8.

### 4. Simulasi Streaming (`stream_simulation.ipynb`)

- Memuat transaksi dari dataset, diurutkan berdasarkan waktu
- Setiap transaksi diproses satu per satu (menyimulasikan data stream)
- Menampilkan **FRAUD ALERT** jika prediksi = fraud
- Memvisualisasikan probabilitas fraud sepanjang aliran transaksi

### 5. Dashboard Streamlit (`dashboard.py`)

Dashboard interaktif untuk menguji prediksi secara manual:
- Input parameter transaksi melalui form
- Mengirim request ke FastAPI
- Menampilkan hasil prediksi: probabilitas fraud & status transaksi

---

## Instalasi & Menjalankan

### Prasyarat

Pastikan environment sudah aktif, kemudian install dependency:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost fastapi uvicorn streamlit joblib pydantic requests
```

### Menjalankan API

```bash
cd api
uvicorn fraud_api:app --reload
```

API akan berjalan di `http://127.0.0.1:8000`
Dokumentasi API tersedia di: `http://127.0.0.1:8000/docs`

### Menjalankan Dashboard

Kembali ke root project, lalu jalankan:

streamlit run Deployment/Fraud_Dashboard.py

Dashboard akan berjalan di:

http://localhost:8501

## Arsitektur Sistem

Sistem terdiri dari tiga komponen utama:

Streamlit Dashboard → FastAPI → Model Machine Learning (XGBoost)
Dashboard mengirim request ke API
API memproses data dan melakukan prediksi
Model mengembalikan hasil ke dashboard

## Fitur Model

Model menggunakan 22 fitur berikut:

```
transaction_amount, transaction_type, location, is_foreign_transaction,
device_type, is_new_device, is_new_location, account_age_days,
avg_transaction_amount, transactions_last_24h, failed_logins_24h,
time_since_last_txn, txn_hour, is_weekend, txn_day, txn_month,
txn_dayofweek, amount_ratio, txn_per_day, account_trust_score,
device_risk, night_transaction
```

---

## Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Machine Learning | XGBoost, Scikit-learn, Imbalanced-learn |
| Data Processing | Pandas, NumPy |
| Visualisasi | Matplotlib, Seaborn |
| API | FastAPI, Uvicorn, Pydantic |
| Dashboard | Streamlit |
| Model Serialization | Joblib |
