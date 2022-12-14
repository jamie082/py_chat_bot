
import nltk
import numpy as np
import random
import string

# https://python.gotrained.com/chatbot-development-python-nltk/
greeting_input_texts = ("hey", "heys", "hello", "morning", "evening", "greetings",)
greeting_reply_texts = ["hey", "hey hows you?", "*nod", "hello there", "ello", "Welcome"]

def reply_greeting(text):

    for word in text.split():
        if word.lower() in greeting_input_texts:
            return random.choice(greeting_reply_texts)

continue_discussion=True
print("Hello, I am a chatbot, I will answer your queries regarding global warming:")
while (continue_discussion==True):
    user_input = input()
    user_input = user_input.lower()
    if(user_input != 'bye'):
        if(user_input == 'thanks' or user_input == 'thank you very much' or user_input == 'thank'):
            continue_discussion=False
            print("Chatbot: Most welcome")
        else:
            if(reply_greeting(user_input) != None):
                print("Chatbot: "+reply_greeting(user_input))
            else:
                print("Chatbot: ", end="")
                print(give_reply(user_input))
                sentence_list.remove(user_input)
    else:
        continue_discussion=False
        print("Chatbot: Take ccare, bye...")
        
