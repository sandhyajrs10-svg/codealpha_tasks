import datetime
import random

print("HELLO! WELCOME TO MY AI CHATBOT")
print("You can ask me basic questions or type 'help' for options.")

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I am fine, thank you for asking!",
    "who are you": "I am Rulebot, your friendly chatbot.",
    "what is your name": "My name is Rulebot.",
    "tell me about Sita": "Sita is a good girl and is pursuing BCA from Future University.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
    "help": "I can answer basic questions like 'who are you', 'what is your name', tell you the time, date, or even learn new replies. Type 'exit' or 'bye' to quit.",
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer show up at work late? It had a hard drive!",
    "Why was the math book sad? Because it had too many problems!",
]

fallback_responses = [
    "I'm still learning, so I don't have an answer for that yet.",
    "That's a good question! I can learn new responses if you tell me.",
    "I don't know the answer right now, but I can try to learn it from you.",
]

exit_keywords = {"bye", "exit", "quit", "goodbye"}


def get_response(question: str) -> str:
    question = question.strip().lower()
    if not question:
        return "Please type something so I can answer."

    if question in exit_keywords:
        return "Goodbye! Have a great day!"

    if "help" in question:
        return responses["help"]
    if "time" in question:
        return datetime.datetime.now().strftime("The current time is %I:%M %p.")
    if "date" in question:
        return datetime.datetime.now().strftime("Today's date is %B %d, %Y.")
    if "joke" in question:
        return random.choice(jokes)

    for key, value in responses.items():
        if key in question:
            return value

    return None


def learn_response(question: str) -> None:
    key = question.strip().lower()
    answer = input("I don't know that yet. What should I reply? ").strip()
    if answer:
        responses[key] = answer
        print("Got it! I'll remember that for next time.")
    else:
        print("No response added. Let's continue.")


def main() -> None:
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Please enter a question or type 'help'.")
            continue

        if any(term in user_input.lower() for term in exit_keywords):
            print("Bot: Goodbye! Have a great day!")
            break

        reply = get_response(user_input)
        if reply:
            print(f"Bot: {reply}")
        else:
            print(f"Bot: {random.choice(fallback_responses)}")
            learn = input("Would you like to teach me how to answer this? (yes/no) ").strip().lower()
            if learn in {"yes", "y"}:
                learn_response(user_input)
            else:
                print("No problem. Ask me something else.")


if __name__ == "__main__":
    main()
