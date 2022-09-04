import pdb
import nltk
# import numpy as np
import random
import string

def small_talk_function():
    print("You entered the function Enter function")

small_talk_responses = {
        "What's your name?": "Hi there {input}",
        }

small_talk = small_talk_responses.values() # walk the value
small_talk = [str (item) for item in small_talk]

# https://python.gotrained.com/chatbot-development-python-nltk/
greeting_input_texts = ("hey", "heys", "hello", "morning", "evening", "greetings", "question")
greeting_reply_texts = ["heyz", "hey hows you?", "*nod", "hello there", "ello", "Welcome", "what is the answer?"]

def reply_greeting(text):
    for word in text.split():
        if word.lower() in greeting_input_texts:
            return random.choice(greeting_reply_texts)

continue_discussion=True
print("BOT: What do you want me to call you?")
user_name = input()
print("Hello, I am a chatbot, I will answer your queries regarding global warming:")
while (continue_discussion==True):
    user_input = input()
    user_input = user_input.lower()
    if(user_input != 'bye'): # string to quit program
        if(user_input == 'thanks' or user_input == 'thank you very much' or user_input == 'thank'):
            continue_discussion=False
            print("Chatbot: Most welcome")
        else:
            if(reply_greeting(user_input) != None):
                print("Chatbot: "+reply_greeting(user_input))
            elif (reply_greeting(user_input) == "jamie"): # if user typed jamie
                small_talk_function()
            else:
                print("Chatbot: ", end="")
                print(reply_greeting(user_input))
                sentence_list.remove(user_input)
    else:
        continue_discussion=False
        print("Chatbot: Take care, bye...")
