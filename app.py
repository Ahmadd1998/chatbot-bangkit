import streamlit as st
import json
import random

with open('dataset/intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write("**Pat Assistant**")
st.sidebar.caption("Fresh Seafood Marketplace")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.title("🦐 Chat dengan Pat")
st.caption("Asisten Seafood IFish")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ketik pesanmu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = prompt.lower()
    
    if any(word in user_input for word in ["quit", "exit", "dah", "bye", "keluar", "selesai"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih! Sampai jumpa lagi 🦐"})
        st.stop()
    
    responded = False
    for intent in data.get("intents", []):
        if any(p.lower() in user_input for p in intent.get("patterns", [])):
            st.session_state.messages.append({"role": "assistant", "content": random.choice(intent["responses"])})
            responded = True
            break
    
    if not responded:
        st.session_state.messages.append({"role": "assistant", "content": "Maaf, Pat belum paham. Coba tanya harga, kesegaran, atau pengiriman ya!"})
