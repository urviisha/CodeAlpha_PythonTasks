def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot made in Python!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def chat():
    print("Chatbot: Hi! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    chat()
