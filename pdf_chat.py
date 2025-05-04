# Streamlit is used to build the web UI and Ollama handles local AI chat
import streamlit as st
import ollama  # Make sure Ollama is running locally with the chosen model

# ----- PAGE CONFIGURATION -----
st.set_page_config(
    page_title="ANSHU'S CHAT BOT (PROJECT 2)", 
    page_icon="🤖", 
    layout="centered"
)

# ----- CUSTOM CSS FOR DARK THEME -----
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
        color: white;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .stChatMessage.user {
        background-color: #1f2937;
        color: white;
    }
    .stChatMessage.assistant {
        background-color: #374151;
        color: white;
    }
    input, textarea {
        font-size: 16px !important;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----- APP TITLE -----
st.title("🤖 ANSHU'S CHAT BOT (PROJECT 2)")

# ----- INITIALIZE SESSION STATE FOR CHAT MESSAGES -----
if "messages" not in st.session_state:
    st.session_state.messages = []  # Format: {"role": "user"/"assistant", "content": "text"}

# ----- DISPLAY PREVIOUS CHAT MESSAGES -----
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----- USER CHAT INPUT -----
user_input = st.chat_input("Say something...")

if user_input:
    # Display user's message in chat and store it
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response using Ollama
    with st.spinner("Thinking..."):
        try:
            # Send chat history to Ollama to generate contextual response
            response = ollama.chat(
                model="llama3",  # Change to any local model like mistral or llama2
                messages=st.session_state.messages
            )
            reply = response["message"]["content"]
        except Exception as e:
            reply = f"Error: {e}"  # Handle errors (e.g., if Ollama isn't running)

    # Display and store AI's reply
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
