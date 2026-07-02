import streamlit as st
import json
import random

# Load intents
with open('dataset/intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

# Sidebar
st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write("**Pat - AI Assistant**")
st.sidebar.caption("Fresh Seafood • Delivered Fast")
st.sidebar.divider()
st.sidebar.write("**Jam Operasional**")
st.sidebar.write("05.00 - 11.00 WIB")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Main UI
st.title("🦐 Chat dengan Pat")
st.caption("Asisten Pintar IFish Seafood")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐\nAda yang bisa Pat bantu hari ini?"}
    ]

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ketik pesanmu di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = prompt.lower()
    
    # Exit
    if any(word in user_input for word in ["quit", "exit", "dah", "bye", "keluar", "selesai", "tutup"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih telah menggunakan Pat! Sampai jumpa lagi 🦐"})
        st.stop()
    
    # Simple matching
    responded = False
    for intent in data.get("intents", []):
        if any(word in user_input for word in [p.lower() for p in intent.get("patterns", [])]):
            response = random.choice(intent["responses"])
            st.session_state.messages.append({"role": "assistant", "content": response})
            responded = True
            break
    
    if not responded:
        st.session_state.messages.append({"role": "assistant", "content": "Maaf, Pat belum paham. Coba tanya tentang **harga**, **kesegaran**, **pengiriman**, atau **jam buka** ya!"})
