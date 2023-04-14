import tkinter as tk
from termcolor import colored
import re
import random
import os
import pygame
import math
import time

allJokes = [
    {
        "joke": 'Why did the tomato turn red?',
        "secondResponse": 'Because it saw the salad dressing!'
    },
    {
        "joke": 'Why do bicycles fall over?',
        "secondResponse": 'Because they’re two-tired!'
    },
    {
        "joke": 'Why did the cookie go to the doctor?',
        "secondResponse": 'Because it was feeling crumbly!'
    },
    {
        "joke": 'Why did the hipster burn his tongue?',
        "secondResponse": 'He drank his coffee before it was cool!'
    },
    {
        "joke": 'What do you call fake spaghetti?',
        "secondResponse": 'An impasta!'
    },
    {
        "joke": 'Why don’t scientists trust atoms?',
        "secondResponse": 'Because they make up everything!'
    },
    {
        "joke": 'What do you call a belt made out of watches?',
        "secondResponse": 'A waist of time!'
    },
    {
        "joke": 'Why did the gym close down?',
        "secondResponse": 'It just didn’t work out!'
    },
    {
        "joke": 'What’s the difference between a poorly dressed man on a trampoline and a well-dressed man on a trampoline?',
        "secondResponse": 'Attire!'
    },
    {
        "joke": 'Why don’t oysters share their pearls?',
        "secondResponse": 'Because they’re shellfish!'
    },
    {
        "joke": 'Why did the banana go to the doctor?',
        "secondResponse": 'Because it wasn’t peeling well!'
    },
    {
        "joke": 'Why did the mushroom go to the party?',
        "secondResponse": 'Because he was a fungi to be with!'
    },
    {
        "joke": 'Why did the coffee file a police report?',
        "secondResponse": 'It got mugged!'
    },
    {
        "joke": 'What do you get when you cross a snowman and a shark?',
        "secondResponse": 'Frostbite!'
    },
    {
        "joke": 'Why don’t scientists trust atoms?',
        "secondResponse": 'Because they make up everything!'
    },
    {
        "joke": 'Why did the golfer wear two pairs of pants?',
        "secondResponse": 'In case he got a hole in one!'
    },
    {
        "joke": 'Why do fish live in saltwater?',
        "secondResponse": 'Because pepper water makes them sneeze!'
    },
    {
        "joke": 'Why did the cookie go to the doctor?',
        "secondResponse": 'Because it was feeling crumbly!'
    },
    {
        "joke": 'Why did the chicken cross the playground?',
        "secondResponse": 'To get to the other slide!'
    },
    {
        "joke": 'Why did the tomato turn red?',
        "secondResponse": 'Because it saw the salad dressing!'
    },
    {
        "joke": 'Why did the teddy bear say no to dessert?',
        "secondResponse": 'Because she was already stuffed!'
    },
    {
        "joke": 'Why did the scarecrow win an award?',
        "secondResponse": 'Because he was outstanding in his field!'
    },
    {
        "joke": 'Why don’t skeletons fight each other?',
        "secondResponse": 'They don’t have the guts!'
    },
    {
        "joke": 'How did the scarecrow win the talent show?',
        "secondResponse": 'He was outstanding in his field',
    }
]


# create a new window
window = tk.Tk()
window.title("Linus Assistant")

# create a text area for the chat history
history_text = tk.Text(window, height=10, state='disabled')
history_text.pack()

# create a text box for the user input
input_text = tk.Entry(window, width=100)
input_text.pack()

def SinCosTan(pattern, talk):
    operation = pattern[0][0]
    numberSCT = float(pattern[0][1])
    if operation == 'sin' or operation == 'sine':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.sin(math.radians(numberSCT))))
    elif operation == 'cos' or operation == 'cosine':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.cos(math.radians(numberSCT))))
    elif operation == 'tan' or operation == 'tangent':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.tan(math.radians(numberSCT))))
    if operation == 'sin-1':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.degrees(math.asin(numberSCT))))
    if operation == 'cos-1':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.degrees(math.acos(numberSCT))))
    if operation == 'tan-1':
        return str(str(operation) + ' ' + str(numberSCT) + ' = ' + str(math.degrees(math.atan(numberSCT))))


def mathing(matches, talk):
    for rmatch in matches:
        match rmatch[1]:
            case '+' | 'plus':
                respondWith = (rmatch[0] + ' + ' + rmatch[2] + ' = ' + str(float(rmatch[0]) + (float(rmatch[2]))))
            case '-' | 'minus':
                respondWith = (rmatch[0] + ' - ' + rmatch[2] + ' = ' + str(float(rmatch[0]) - (float(rmatch[2]))))
            case '*' | 'x' | 'times':
                respondWith = (rmatch[0] + ' x ' + rmatch[2] + ' = ' + str(float(rmatch[0]) * (float(rmatch[2]))))
            case '/' | 'divided' | 'divided by':
                respondWith = (rmatch[0] + ' ÷ ' + rmatch[2] + ' = ' + str(float(rmatch[0]) / (float(rmatch[2]))))
            case '^' | 'to the power of' | 'exponent' | '**':
                respondWith = (rmatch[0] + '^' + rmatch[2] + ' = ' + str(float(rmatch[0]) ** (float(rmatch[2]))))
    return respondWith


def chooseJoke():
    joke = random.choice(allJokes)
    return [joke["joke"], joke["secondResponse"]]

responses = [
    {
        "input": ['hi','hello','sup',"wassup","hey","whats up",'hi linus','hello linus','sup linus',"wassup linus","hey linus","whats up linus"], #Never put capital letters or punctuation inside "input", Also make sure to add many options
        "responses": ["Hello!", "Hi there!", "Hey!", "Hi!"], #Use correct grammer, with multiple responses. Try not to add many questions, but if you do, than make sure to add a new "input" with what the user would answer with
    },
    {
        "input": ["how are you", "how are you linus", "are you okay", "how do you do", "how are you feeling", "how are you doing", "how are you doing today","how are you feeling today"],
        "responses": ["I'm good, thank you!", "I'm doing well!", "I'm fine, how about you?"],
    },
    {
        "input": ["good","awesome","epic","great","im good how about you", "im good","im awesome","im epic","im great","im fine", "fine"],
        "responses": ["That's great!", "Good."],
    },
    {
        "input": ["whats your name", "what is your name", "can you tell me your name", "may I know your name"],
        "responses": ["I'm Linus?","My name is Linus, nice to meet you!"],
    },
    {
        "input": ["what can you do", "what are your abilities", "what's your function", "what's your purpose"],
        "responses": ["I can do math, play songs, tell jokes, and even roast you!"]
    },
    {
        "input": ["what do you like", "what's your favorite thing", "what do you enjoy"],
        "responses": ["As a chatbot, I don't have personal preferences or emotions.", "I don't have likes or dislikes, I just respond based on the input I receive."],
    },
    {
        "input": ["what is your favorite food", "whats your favorite food", "whats your favorite food to eat"],
        "reponse": ["I have never tried any!"],
    },
    {
        "input": ["what is your favorite number","whats your favorite number"],
        "response": ["My favorite number is 56!"],
    },
    {
        "input": ["bye", "goodbye", "see you later", "talk to you later"],
        "responses": ["Goodbye!", "Bye!", "See you later!", "Take care!"],
    },
    {
        "input" : ["linus"],
        "response": ["Yes?", "That's my name!"],
    },
    {
        "input": ['tell me a joke', 'joke', 'tell me another joke'],
        "action": 'chooseJoke',
    },
    {
        "input": ["what is your name","whats your name","your name","who are you"],
        "responses": ["You can call me Linus","My name is Linus", "I'm Linus!","I'm Linus, how are you?"],
    },
    {
        "input": ["roast me", "give me a roast", "another roast", "roast"],
        "action": 'chooseRoast',
    },
    # {
    #     "input": ["stop", "stop playing", "stop song"],
    #     "action": 'stopSong',
    # },
    # {
    #     "input": ["pause", "pause playing", "pause song"],
    #     "action": 'pauseSong',
    # },
    # {
    #     "input": ["resume", "resume song", "resume playing", "continue song", "continue playing", "continue"],
    #     "action": 'resumeSong',
    # },
    # {
    #     "input": ["play", "play song"],
    #     "action": 'resumeSong',
    # },
    # {
    #     "input": ["play", "play song"],
    #     "action": 'resumeSong',
    # },
    # {
    #     "input": ["restart", "restart song", "start over", "play again"],
    #     "action": "restartSong",
    # },
    # {
    #     "input": ["list the songs you can play", "list songs", "song list", 'list your songs', "list all songs","list the songs", "songs list", "give me a list of the songs you can play", 'list the songs you can play'],
    #     "action": "listTheSongs",
    # },
    {
        "regex": r'(\d*\.?\d+)\s*(\*|x|\/|\+|-|\^|\*\*|times|minus|plus|divide|divided by|to the power of|exponent)\s*(\d*\.?\d+)',
        "action": "mathing",
    },
    {
        "regex": r'(sin|cos|tan|sin-1|cos-1|tan-1|sine|cosine|tangent|sine-1|cosine-1|tangent-1)\s*(?:of)?\s*(\d*\.?\d+)',
        "action": "SinCosTan",
    },
    {
        "regex": r'^(?:hi|hello)?\s*(?:,|\.)*\s*(?:linus)?\s*(?:,|\.)*\s*(?:im|my names|my name is)\s*(\w*\s*)',
        "action": 'responseHello', 
    },
    # {
    #     "regex": r'(^play)\s*((the song)?(?:song)?)\s*([\w\s]*)',
    #     "action": "playSong",
    # },
]

defaultResponse = ["I'm sorry, I don't understand.","I'm not sure I follow?","I don't understand, make sure you spelled it right..."]

def chatbot_response(talk, untalk):
    global respondWith, message, response
    for response in responses:
        
        if "regex" in response:
            regexMatches = re.findall(response['regex'], untalk) 
            if regexMatches:
                if "action" in response:
                    func = globals()[response['action']]
                    return func(regexMatches, talk)
                elif "responses" in response:  
                    
                    return random.choice(response["responses"])
                    
                

        elif talk in (re.sub(r'[^\w\d]', '', _) for _ in response['input']):
            if "action" in response:
                func = globals()[response['action']]
                return func()
            else:
                return random.choice(response["responses"])
        
    return random.choice(defaultResponse)
        



def send_message():
    global message, response
    message = input_text.get()
    untalk = message.lower()
    talk = re.sub(r'[^\w\d]', '', untalk)
    response = chatbot_response(talk, untalk)

    if "action" in response and response["action"] == chooseJoke:
        respondWith = chooseJoke()
        history_text.insert('end', 'Linus: ')
        history_text.insert('end', f'{respondWith[0]} \n', ('response'))
        time.sleep(2)
        history_text.insert('end', f'{respondWith[1]} \n \n', ('response'))
    else:
        if untalk.lower() == "!end":
            return
        history_text.configure(state='normal')
        history_text.insert('end', 'You: ')
        history_text.insert('end', message + '\n', ('user'))
        history_text.insert('end', 'Linus: ')
        history_text.insert('end', f'{response} \n \n', ('response'))
        history_text.configure(state='disabled')
        input_text.delete(0, tk.END)





input_text.bind("<Return>", lambda event: send_message())

button = tk.Button(window, text="Ask", command=send_message)
button.config(height=2, width=5, bg='gray', fg='dark red')
button.pack()



# configure tags for colored text
history_text.tag_config('user', foreground='blue')
history_text.tag_config('response', foreground='red')
history_text.configure(state='disabled')


# run the window
window.mainloop()
