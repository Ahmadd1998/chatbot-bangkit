import streamlit as st
import json
import random

# 1. Gunakan cache supaya JSON tidak dibaca ulang setiap kali ada interaksi (mencegah lag)
@st.cache_data
def load_intents():
    with open('dataset/intents.json', 'r', encoding='utf-8') as f:
        return json.load(f)

data = load_intents()

st.set_page_config(page_title="IFish Chatbot", page_icon="🦐", layout="centered")

st.sidebar.title("🦐 IFish Seafood")
st.sidebar.write("**Pat Assistant**")
st.sidebar.caption("Fresh Seafood Marketplace")

# 2. Fix Clear Chat: Langsung isi dengan pesan awal, jangan dikosongkan []
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐"}]
    st.rerun()

st.title("🦐 Chat dengan Pat")
st.caption("Asisten Seafood IFish")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐"}]

# Render riwayat obrolan
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 3. Logika Input
if prompt := st.chat_input("Ketik pesanmu..."):
    # Simpan input user
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = prompt.lower()
    
    # Cek kalimat keluar
    if any(word in user_input for word in ["quit", "exit", "dah", "bye", "keluar", "selesai"]):
        st.session_state.messages.append({"role": "assistant", "content": "Terima kasih! Sampai jumpa lagi 🦐"})
        st.rerun() # Langsung render lalu stop
        st.stop()
    
    # Cek intensi/pola jawaban
    responded = False
    for intent in data.get("intents", []):
        if any(p.lower() in user_input for p in intent.get("patterns", [])):
            st.session_state.messages.append({"role": "assistant", "content": random.choice(intent["responses"])})
            responded = True
            break
    
    # Jika tidak ada yang cocok
    if not responded:
        st.session_state.messages.append({"role": "assistant", "content": "Maaf, Pat belum paham. Coba tanya harga, kesegaran, atau pengiriman ya!"})
    
    # 4. WAJIB RERUN: Paksa UI refresh untuk menampilkan pesan baru tanpa delay
    st.rerun()
