import streamlit as st
import json
import random
import nltk
from nltk.stem import LancasterStemmer

# ================== NLTK SETUP ==================
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)   # Fix untuk error ini

stemmer = LancasterStemmer()

# Load intents
with open('dataset/intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Preprocess function
def preprocess(text):
    return [stemmer.stem(word.lower()) for word in nltk.word_tokenize(text)]

# Preprocess all patterns
intent_patterns = []
for intent in data.get("intents", []):
    patterns = [preprocess(p) for p in intent.get("patterns", [])]
    intent_patterns.append({
        "tag": intent["tag"],
        "patterns": patterns,
        "responses": intent["responses"]
    })

# ================== STREAMLIT UI ==================
st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write("**Pat - AI Assistant**")
st.sidebar.caption("Fresh Seafood Marketplace")
st.sidebar.divider()

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.title("🦐 Chat dengan Pat")
st.caption("Asisten Pintar IFish Seafood")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐\nAda yang bisa Pat bantu hari ini?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ketik pesanmu di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = preprocess(prompt)
    
    # Exit detection
    if any(word in prompt.lower() for word in ["quit", "exit", "dah", "bye", "keluar", "selesai", "tutup"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih telah chat dengan Pat! Sampai jumpa lagi 🦐"})
        st.stop()
    
    # Intent matching
