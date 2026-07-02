# 🦐 IFish Seafood Chatbot (Aplikasi Web Streamlit)

---

## Versi Bahasa Indonesia

Chatbot asisten virtual untuk toko **IFish Seafood**. Proyek ini sebelumnya menggunakan Deep Learning, namun telah dibangun ulang sepenuhnya menjadi aplikasi web interaktif menggunakan **Streamlit** dengan pendekatan *Rule-Based (Pencocokan Kata Kunci)*. Tujuannya adalah membuat aplikasi menjadi lebih ringan, lebih responsif, dan lebih mudah di-*deploy* tanpa memerlukan pelatihan model yang berat.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red)
![Status](https://img.shields.io/badge/Status-Active-success)

### ✨ Fitur Utama
Coba Demonya di sini: [https://chatbot-ifish.streamlit.app/](https://chatbot-ifish.streamlit.app/)

*   **UI Berbasis Web:** Antarmuka obrolan interaktif yang menyerupai aplikasi obrolan modern.
*   **Pencocokan Intent Berbasis Aturan (Rule-Based):** Merespons masukan pengguna berdasarkan deteksi kata kunci secara instan.
*   **27+ Skenario Percakapan:** Mencakup informasi mengenai harga, ketersediaan stok, lokasi, pengiriman, promo, komplain, hingga status *seafood* hidup.
*   **Efisiensi Tinggi:** Berjalan murni menggunakan Python Standard Library dan Streamlit (tanpa dependensi *machine learning* yang berat).

### 🛠 Teknologi yang Digunakan
*   **Python 3.8+**
*   **Streamlit** (Front-end & Framework Web)
*   **JSON** (Penyimpanan data *intent* & respons)

### 📁 Struktur Proyek
```text
proyek-chatbot/
│
├── dataset/
│   └── intents.json      # File database untuk skenario & respons chatbot
├── app.py                # Script utama aplikasi Streamlit
└── requirements.txt      # Daftar dependensi (streamlit)
```

### 🚀 Instalasi & Setup Lokal

1. Clone Repository

```
Bash
git clone https://github.com/Ahmadd1998/chatbot-bangkit
cd proyek-chatbot
```

2. Install Dependensi

```
Bash
pip install -r requirements.txt
```

3. Jalankan Aplikasi

```
Bash
streamlit run app.py
```

Aplikasi akan otomatis terbuka di browser kamu pada alamat http://localhost:8501.

### 📊 Dataset

Dataset menggunakan format JSON (dataset/intents.json) yang terdiri dari 27 intent percakapan. Menambahkan skenario baru atau memperbarui harga dapat dilakukan secara instan dengan mengedit file JSON ini tanpa perlu melatih ulang algoritma apa pun.

### 👥 Kontributor

Ahmad Gozali Abbas — Pengembang Utama

### 📄 Lisensi

Open-source untuk keperluan edukasi dan portofolio. Dibuat dengan 🦐 menggunakan Streamlit.
