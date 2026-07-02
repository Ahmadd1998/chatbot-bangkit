# 🦐 IFish Seafood Chatbot (Streamlit Web App)

---

A virtual assistant chatbot for the **IFish Seafood** store. This project previously used Deep Learning but has been completely rebuilt into an interactive web application using **Streamlit** with a *Rule-Based (Keyword Matching)* approach. The goal is to make the application lighter, more responsive, and easier to deploy without the need for heavy model training.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red)
![Status](https://img.shields.io/badge/Status-Active-success)

### ✨ Key Features
Try the Demo here: [https://chatbot-ifish.streamlit.app/](https://chatbot-ifish.streamlit.app/)

- **Web-Based UI:** Interactive chat interface resembling modern chat apps.
- **Rule-Based Intent Matching:** Responds to user input based on instant keyword detection.
- **27+ Conversation Scenarios:** Covers information on prices, stock availability, location, shipping, promos, complaints, and live seafood status.
- **High Efficiency:** Runs purely using the Python Standard Library and Streamlit (no heavy machine learning dependencies).

### 🛠 Technologies Used
- **Python 3.8+**
- **Streamlit** (Front-end & Web Framework)
- **JSON** (Intent & response data storage)

### 📁 Project Structure
```text
proyek-chatbot/
│
├── dataset/
│   └── intents.json      # Database file for chatbot scenarios & responses
├── app.py                # Main Streamlit application script
└── requirements.txt      # List of dependencies (streamlit)
```
### 🚀 Installation & Local Setup

1. Clone Repository

```
Bash
git clone https://github.com/Ahmadd1998/chatbot-bangkit
cd proyek-chatbot
```

2. Install Dependencies

```
Bash
pip install -r requirements.txt
```

3. Run the Application

```
Bash
streamlit run app.py
```

The application will automatically open in your browser at http://localhost:8501.

### 📊 Dataset

The dataset uses a JSON format (dataset/intents.json) consisting of 27 conversation intents. Adding new scenarios or updating prices can be done instantly by editing this JSON file without retraining any algorithms.

### 👥 Contributor

Ahmad Gozali Abbas — Lead Developer

### 📄 License

Open-source for educational and portfolio purposes. Built with 🦐 using Streamlit.
