#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define patterns and responses
    patterns = {
        r"hello|hi|hey": "Hello! How can I help you?",
        r"how are you": "I'm a computer program, so I don't have feelings, but thanks for asking!",
        r"what is your name": "I'm a simple chatbot.",
        r"bye|goodbye": "Goodbye! Have a great day!",
        r"thanks|thank you": "You're welcome!",
        r"(.*) your name(.*)": "I'm a simple chatbot.",
        r"(.*) age(.*)": "I don't have an age. I'm just a program.",
        r"(.*) (love|like) (.*)": "I'm just a machine, so I don't experience emotions, but I'm here to assist you!",
        # Add more patterns and responses as needed
    }

    # Check for matches and return the corresponding response
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    # Default response for unrecognized queries
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Simple loop to simulate a conversation
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Simple Chatbot:", response)


# In[ ]:




