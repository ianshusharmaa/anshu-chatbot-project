# Importing the 'requests' module to send HTTP requests to the local Ollama API
import requests

# This function sends user input (prompt) to the locally running Ollama AI model
def chat_with_ollama(prompt):
    response = requests.post(
        'http://localhost:11434/api/generate',  # Local server where Ollama is running
        json={
            'model': 'mistral',      # Using the 'mistral' model for response
            'prompt': prompt,        # What the user typed
            'stream': False          # Not using streaming; waiting for full response
        }
    )
    return response.json()['response']  # Extracting and returning the AI's reply

# Main chat loop
print("Offline Chat (type 'exit' to quit):")
while True:
    user_input = input("You: ")  # Taking input from the user
    if user_input.lower() == 'exit':
        break  # Exit the loop if user types 'exit'

    reply = chat_with_ollama(user_input)  # Get response from AI
    print("AI:", reply)  # Display the AI's response
