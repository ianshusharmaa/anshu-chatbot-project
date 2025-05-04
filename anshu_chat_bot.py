
import streamlit as st
import ollama

# Configure Streamlit page
st.set_page_config(page_title="ANSHU'S CHAT BOT (PROJECT 2)", page_icon="🤖", layout="centered")

# Custom CSS for styling
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

st.title(" ANSHU'S CHAT BOT (PROJECT 2)")

# Store messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Say something...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            response = ollama.chat(
                model="llama3",
                messages=st.session_state.messages
            )
            reply = response["message"]["content"]
        except Exception as e:
            reply = f"Error: {e}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
