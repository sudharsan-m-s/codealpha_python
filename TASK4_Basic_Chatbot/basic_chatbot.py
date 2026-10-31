"""A small rule-based chatbot using predefined replies."""

RESPONSES = {
    "hello": "Hi!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks! How can I help?",
    "what is your name": "I'm a simple Python chatbot.",
    "bye": "Goodbye!",
}


def get_response(message: str) -> str:
    """Return a predefined response for supported phrases."""
    normalized_message = " ".join(message.lower().strip().split())
    return RESPONSES.get(normalized_message, "I don't know that one yet. Try 'hello', 'how are you', or 'bye'.")


def chat() -> None:
    print("Basic Chatbot - type 'bye' to exit.")
    while True:
        message = input("You: ")
        response = get_response(message)
        print(f"Bot: {response}")
        if " ".join(message.lower().strip().split()) == "bye":
            break


def main() -> None:
    chat()


if __name__ == "__main__":
    main()
