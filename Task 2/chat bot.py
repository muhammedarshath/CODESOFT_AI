def rule_based_chatbot():
    print("Chatbot: Hi! I'm a rule-based bot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye" or user_input == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing well! How about you?")
        elif "name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot built with Python.")
        elif "weather" in user_input:
            print("Chatbot: I can't access real-time data, but it looks like a nice day for coding!")
        else:
            print("Chatbot: Sorry, I don't understand. Try rephrasing or ask about something else.")

# Run the chatbot
rule_based_chatbot()
