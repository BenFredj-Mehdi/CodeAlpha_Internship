import nltk
from nltk.chat.util import Chat, reflections

# Define some reflections to make the conversation more natural
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define some patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["Apologies are not necessary.", "No need to apologize.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem.",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'd be happy to help. What do you need assistance with?",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye, take care!"]
    ],
]

# Create a chatbot using the defined patterns and reflections
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Welcome! Type 'quit' to exit.")
test=True
while test:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input == "quit" :
        test=False
