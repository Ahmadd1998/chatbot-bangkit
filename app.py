import streamlit as st
import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tflearn
import tensorflow as tf

nltk.download('punkt', quiet=True)
stemmer = LancasterStemmer()

st.set_page_config(page_title="IFish Chatbot", page_icon="🦐")

# Load dataset
with open('dataset/intents.json') as file:
    data = json.load(file)

# Load training data
with open("data.oke", "rb") as f:
    words, labels, training, output = pickle.load(f)

# Load model
tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)
model.load("model.tflearn")

st.title("🦐 IFish Chatbot - TensorFlow Version")
st.caption("Powered by Bangkit 2021 Model")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Halo! Selamat datang di IFish Seafood 🦐"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ketik pesanmu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    bag = [0] * len(words)
    s_words = nltk.word_tokenize(prompt)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    results = model.predict([bag])[0]
    results_index = np.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == tag:
            response = random.choice(tg['responses'])
            st.session_state.messages.append({"role": "assistant", "content": response})
            break
