pip install nltk

import random
import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files (only need to run once)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?", "Nice to meet you %1! What would you like to learn today?"]
    ],
    [
        r"what is your name?",
        ["I am an educational chatbot created to help you learn!"]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking! How can I assist you today?"]
    ],
    [
        r"what can you teach me?",
        ["I can help you with various subjects like Math, Science, History, and more! What are you interested in?"]
    ],
    [
        r"tell me about (.*)",
        ["%1 is a fascinating topic! What specifically would you like to know about %1?"]
    ],
    [
        r"what is (.*)?",
        ["%1 is a concept that can be defined as follows: ... (Please ask me for specific details!)"]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please ask me something else?"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I am an educational chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()