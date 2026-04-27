# 🛡️ End-to-End Real-Time Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-black?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

Proyek ini adalah sistem deteksi penipuan (fraud) transaksi keuangan yang komprehensif, mencakup seluruh pipeline data science mulai dari pembersihan data mentah hingga penyediaan layanan prediksi real-time melalui API dan Dashboard interaktif.

---

## 🚀 Alur Kerja Sistem (Pipeline)



[Image of Machine Learning Pipeline]


### 1. Data Analytics & Cleaning
Melakukan eksplorasi data (EDA) untuk memahami pola transaksi.
* **Pembersihan Data:** Menangani nilai yang hilang (missing values) dengan median untuk numerik dan mode untuk kategorikal.
* **Visualisasi:** Analisis korelasi, distribusi jumlah transaksi, dan perbandingan antara transaksi normal vs fraud.

### 2. Advanced Feature Engineering
Menciptakan fitur baru untuk meningkatkan daya prediksi model:
* **Amount Ratio:** Rasio transaksi saat ini dibanding rata-rata transaksi user.
* **Device Risk:** Skor risiko berdasarkan penggunaan perangkat baru, lokasi baru, atau transaksi luar negeri.
* **Time Features:** Mengekstrak jam transaksi untuk mendeteksi `night_transaction` (transaksi tengah malam yang berisiko tinggi).
* **Account Trust Score:** Menghitung tingkat kepercayaan akun berdasarkan umur akun dan jumlah gagal login.

### 3. Balancing Data (SMOTE)
Karena data fraud biasanya sangat sedikit (imbalanced), sistem ini menggunakan **SMOTE (Synthetic Minority Over-sampling Technique)** untuk menyeimbangkan jumlah data fraud dan normal agar model tidak bias.

### 4. Model Training & Optimization (XGBoost)
* Menggunakan algoritma **XGBoost Classifier**.
* **Hyperparameter Tuning:** Menggunakan `GridSearchCV` dengan `StratifiedKFold` untuk mencari parameter terbaik (max_depth, learning_rate, dll).
* **Evaluasi:** Model dievaluasi menggunakan *Confusion Matrix*, *ROC-AUC Curve*, dan *Feature Importance*.

### 5. Deployment & Simulation
* **FastAPI:** Menyediakan endpoint `/predict` untuk menerima data transaksi dalam format JSON dan mengembalikan probabilitas fraud.
* **Streamlit Dashboard:** Antarmuka visual untuk mensimulasikan transaksi secara langsung oleh pengguna.
* **Real-Time Stream Simulation:** Skrip simulasi untuk memproses ribuan data transaksi seolah-olah data masuk secara terus-menerus.

---

## 📂 Struktur Folder

```bash
.
├── 📊 Analyst Data/       # EDA, Cleaning, & df_clean.csv
├── 🧪 Modeling Data/      # Feature Engineering, SMOTE, Training, & Save Model (.pkl)
├── 🔌 API/                # Production code dengan FastAPI
├── 🚀 Deployment/         # Dashboard interaktif Streamlit
└── 📁 Data/               # Dataset mentah (Raw Data)
