responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    # Add more responses here
}

def chat():
    print("Chatbot: Hello! How can I assist you?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = responses.get(user_input, "Chatbot: I'm not sure how to respond to that.")
        print(response)

if __name__ == "__main__":
    chat()
