import streamlit as st
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

st.title("AI Programming Assistant")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant specialized in AI and programming."}
    ]

# Display previous messages
for message in st.session_state.messages[1:]:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=st.session_state.messages,
        model=MODEL_NAME
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(reply)