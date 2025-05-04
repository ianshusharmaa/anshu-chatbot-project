import requests

def chat_with_ollama(prompt):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'mistral',
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()['response']

print("Offline Chat (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    reply = chat_with_ollama(user_input)
    print("AI:", reply)