# 🦐 Seafood Chatbot (TensorFlow & TFLearn)

Chatbot cerdas berbasis **Deep Learning** yang dirancang untuk menjawab pertanyaan seputar produk seafood seperti **harga, kesegaran, daya tahan, jam operasional, dan pengiriman**.  
Proyek ini menggunakan **TensorFlow** dan **TFLearn** untuk melakukan *intent classification* berdasarkan input teks pengguna.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.5-orange)
![Status](https://img.shields.io/badge/Status-Educational-success)

---

## ✨ Fitur Utama
Bisa cobain Demo disini yaa : https://chatbot-ifish.streamlit.app/
- Klasifikasi intent menggunakan neural network
- Mendukung variasi kalimat (tidak harus persis sama dengan dataset)
- Chat interaktif berbasis terminal
- Mudah dikembangkan dengan menambah intent baru

---

## 🛠 Teknologi yang Digunakan
- **Python** 3.7+
- **TensorFlow** 2.5.0
- **TFLearn** 0.5.0
- **NLTK** (Natural Language Processing)
- **NumPy**

---

## 📁 Struktur Proyek
```
proyek-chatbot/
│
├── main.ipynb
├── chatsss.json
├── data.oke
├── model.tflearn
├── model.tflearn.meta
└── README.md
```

---

## 🚀 Instalasi & Setup

### Clone Repository
```bash
git clone <repository-url>
cd proyek-chatbot
```

### Install Dependencies
```bash
pip install nltk numpy tflearn tensorflow
```

### Download Data NLTK
```python
import nltk
nltk.download('punkt')
```

---

## 🧠 Training Model
Buka `main.ipynb` lalu jalankan seluruh cell.

Model akan tersimpan sebagai:
- `model.tflearn`
- `data.oke`

### Arsitektur Model
- Input layer: panjang vocabulary
- Hidden layer: 2 fully connected layer (8 neuron)
- Output layer: softmax
- Optimizer: Adam
- Epoch: 1000
- Batch size: 8

---

## 💬 Penggunaan Chatbot
```python
chat()
```

Contoh:
```
You: Hi
Bot: Hello!
```

Ketik `quit` untuk keluar.

---

## 📊 Dataset
Dataset `chatsss.json` terdiri dari 10 intent:
greeting, goodbye, thanks, name, shop, hours, price, fresh, durable, deliver.

---

## 📈 Performa
- Akurasi training: ~100%
- Loss: ~0.007

---

## 📌 Catatan
- Menggunakan LancasterStemmer
- Dataset dapat diperluas
- Untuk produksi disarankan LSTM / Transformer

---

## 👥 Kontributor
**Ahmad 21** — Pengembang Utama

---

## 📄 Lisensi
Open-source untuk keperluan edukasi.

Dibuat dengan ❤️ menggunakan TensorFlow & TFLearn
