import streamlit as st
import json
import random

# Load intents
with open('intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

# Sidebar
st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write(f"**{data['chatbot_name']}**")
st.sidebar.write("Fresh Seafood | Setiap Hari")
st.sidebar.divider()
st.sidebar.write("**Jam Operasional**")
st.sidebar.write("05.00 - 11.00 WIB")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Main Chat
st.title("🦐 Chat dengan Pat")
st.caption("Asisten IFish Seafood - Tanya harga, ketersediaan, pengiriman, dll.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood. Ada yang bisa Pat bantu hari ini? 🦐"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ketik pesanmu di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Process response
    user_input = prompt.lower().strip()
    responded = False
    
    # Exit check
    if any(word in user_input for word in ["quit", "exit", "dah", "bye", "keluar", "selesai", "tutup"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih telah menggunakan layanan Pat! Sampai jumpa lagi 🦐"})
        st.stop()
    
    # Intent matching
    for intent in data["intents"]:
        if any(word in user_input for word in [p.lower() for p in intent.get("patterns", [])]):
            response = random.choice(intent["responses"])
            st.session_state.messages.append({"role": "assistant", "content": response})
            responded = True
            break
    
    if not responded:
        st.session_state.messages.append({"role": "assistant", "content": "Maaf, Pat belum paham pertanyaanmu. Coba tanya seputar harga, kesegaran, pengiriman, atau jam buka ya!"})
