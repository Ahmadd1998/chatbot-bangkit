import streamlit as st
import json
import random
import nltk
from nltk.stem import LancasterStemmer

# Download NLTK (hanya sekali)
nltk.download('punkt', quiet=True)

stemmer = LancasterStemmer()

# Load intents dari folder dataset
with open('dataset/intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Preprocess patterns
def preprocess(text):
    return [stemmer.stem(word.lower()) for word in nltk.word_tokenize(text)]

# Preprocess semua patterns
intent_patterns = []
for intent in data.get("intents", []):
    patterns = [preprocess(p) for p in intent.get("patterns", [])]
    intent_patterns.append({
        "tag": intent["tag"],
        "patterns": patterns,
        "responses": intent["responses"]
    })

# === Streamlit UI ===
st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write("**Pat - AI Assistant**")
st.sidebar.caption("Fresh from Sea to Your Table")
st.sidebar.divider()

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.title("🦐 Chat dengan Pat")
st.caption("Asisten Pintar IFish Seafood")

# Inisialisasi chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐\nAda yang bisa Pat bantu hari ini?"}
    ]

# Tampilkan pesan
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input user
if prompt := st.chat_input("Ketik pesanmu di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = preprocess(prompt)
    responded = False
    
    # Exit detection
    if any(word in prompt.lower() for word in ["quit", "exit", "dah", "bye", "keluar", "selesai", "tutup"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih telah chat dengan Pat! Sampai jumpa lagi 🦐"})
        st.stop()
    
    # Matching
    best_match = None
    highest_overlap = 0
    
    for intent in intent_patterns:
        for pattern in intent["patterns"]:
            overlap = len(set(user_input) & set(pattern))
            if overlap > highest_overlap:
                highest_overlap = overlap
                best_match = intent
    
    if best_match and highest_overlap > 0:
        response = random.choice(best_match["responses"])
    else:
        response = "Maaf, Pat belum mengerti. Coba tanya tentang **harga**, **kesegaran**, **pengiriman**, atau **jam buka** ya!"
    
    st.session_state.messages.append({"role": "assistant", "content": response})
