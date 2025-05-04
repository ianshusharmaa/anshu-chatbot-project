import streamlit as st
import requests

st.set_page_config(page_title="Offline ChatGPT Clone")

st.title("Offline ChatGPT Clone (Mistral)")

# Initialize session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    # Save user message
    st.session_state.chat_history.append(("You", user_input))

    # Send to Ollama
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'mistral',
            'prompt': user_input,
            'stream': False
        }
    )
    ai_response = response.json()['response']

    # Save AI response
    st.session_state.chat_history.append(("AI", ai_response))

# Display full conversation
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**AI:** {message}")
