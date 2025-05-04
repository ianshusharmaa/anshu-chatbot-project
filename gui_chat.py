# Streamlit for web app UI and requests to communicate with local Ollama model
import streamlit as st
import requests

# Set page title shown in browser tab
st.set_page_config(page_title="Offline ChatGPT Clone")

# Main title on the app
st.title("Offline ChatGPT Clone (Mistral Model)")

# Initialize chat history when app loads for the first time
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Store tuples of (speaker, message)

# Input box for user to type message
user_input = st.text_input("You:")

# When user types something
if user_input:
    # Add user's message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # Send request to local Ollama API (running on port 11434)
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'mistral',         # Specify the model to use
            'prompt': user_input,       # User's message
            'stream': False             # Get full response (no streaming)
        }
    )

    # Extract AI's reply from response JSON
    ai_response = response.json()['response']

    # Add AI's response to chat history
    st.session_state.chat_history.append(("AI", ai_response))

# Display the full chat history in order
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**AI:** {message}")
