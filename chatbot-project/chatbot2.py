import random
from termcolor import colored
import os
os.system('cls')
text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])
import nltk
# if not nltk.corpus.wordnet.exists():
    # download wordnet resource
print(text_linus + "Linus will need to install a database for many features to work, please wait... Do not close the app")
nltk.download('wordnet')
print("\n")

from nltk.corpus import wordnet
import re
import sys
import pygame
from email.message import EmailMessage
import ssl
import smtplib
import time
from pong import pongGame
from TicTacToe1p import tic_tac_toe1p
from TicTacToe2p import tic_tac_toe2p
from countryData import CCCdatbase
import math
os.system("cls")



abilities = ["""
I can do many things, some things I can do are:
> list songs
Math (ex. 5*5, 8^3, 9/4)
Games (ex. pong, tic tac toe)
> 
"""]


def tic_tac_toe():
    tictactoe1_2 = input(text_linus + "Would you like to play tic tac toe 1 player or 2 player? [1/2/quit]: ")
    if '1' in tictactoe1_2:
        return tic_tac_toe1p()
    elif '2' in tictactoe1_2:
        return tic_tac_toe2p()
        
    else:
        return "Canceled"


current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])

songList = ["bang.mp3","just like you.mp3","karma.mp3","paid my dues.mp3","the good part.mp3"]

def countryDataReverse(pattern):
    query = re.sub(r'[^\w\d]', '', pattern[0][1].lower())
    for country in CCCdatbase:
        if pattern[0][0] == 'capital':
            field = re.sub(r'[^\w\d]', '', country["capital"].lower())
        else:
            field = re.sub(r'[^\w\d]', '', country["currency"].lower())

        if field == query:
            if isinstance(country["country"],str):
                countryName = country["country"]
            else:
                countryName = country["country"][0]
            if pattern[0][0] == 'capital':
                return f"{country['capital']} is the capital of {countryName}."
            else:
                return f"{country['currency']} is the currency of {countryName}."
    return "No matching countries!"

def countryData(pattern):
    countryName = re.sub(r'[^\w\d]', '', pattern[0][1].lower())
    for country in CCCdatbase:
        if isinstance(country["country"],str):
            countryVersions = [country["country"]]
        else:
            countryVersions = country["country"]
        for countryVersion in countryVersions:
            countryDict = re.sub(r'[^\w\d]', '', countryVersion.lower())

            if countryDict == countryName:
                if pattern[0][0] == 'capital':
                    return f"The capital of {countryVersion} is {country['capital']}."
                else:
                    return f"The currency of {countryVersion} is {country['currency']}."
    return "Country Not Found!"



def playSong(pattern):
    patternSongPlaying = pattern[0][3]
    pygame.init()
    if (patternSongPlaying + '.mp3') in songList:
        pygame.mixer.music.load(patternSongPlaying + '.mp3')
        pygame.mixer.music.play()
        return ("Playing " + patternSongPlaying)
    else:
        return "We don't have that song! Try asking 'song request'."

def listTheSongs():
    for i, song in enumerate(songList, start=1):
        print(colored(f"{i}. ", 'red', attrs=['bold','dark']) + song[:-4])
    return "Those are the songs you can play!"

def songRequests():
    songRequestY_N = input(text_linus + "Would you like to make a song request? [y/n]: ")
    if 'y' in songRequestY_N:
        theRequest = input(text_linus + "What song would you like to request? Include author and full song name: ")

        email_sender = 'linuschatbot@gmail.com'
        #code, do not share
        email_password = 'wtockzyhzehlrigl'
        #reciever (also forwarded to jstark09@nca.edu.ni, using filters in judahstarkenburg@gmail.com account)
        email_reciever = 'judahstarkenburg@gmail.com'

        #input the users email
        user_email = input(text_linus + "Enter YOUR Email To Recieve Further Information About The Song Request Made (Required!): ")
        
        #check if its a valid email adress, if it is, send it with body text and info
        if '@gmail.com' in user_email or '@yahoo.com' in user_email or '@nca.edu.ni' in user_email or '@hotmail.com' in user_email:
            subject = '<Linus> New Song Request!'
            body = ("""
            ----------------------
            Someone Has Requested For The Song: 
            """ + theRequest + """
            ----------------------
            Person Who Requested: 
            """ + user_email)

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_reciever
            em['Subject'] = subject
            em.set_content(body)

            thecontext = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=thecontext) as smtp:
                time.sleep(.3)
                print(text_linus + 'Loading... This might take a while!')
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, em.as_string())
                time.sleep(1)
                return "Song request made!"
        else:
            return "Invalid email!"
    else:
        return "Canceled!"

def SinCosTan(pattern):
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
    


def mathing(matches):
    for rmatch in matches:
        match rmatch[1]:
            case '+' | 'plus':
                print(text_linus + (rmatch[0] + ' + ' + rmatch[2] + ' = ' + str(float(rmatch[0]) + (float(rmatch[2])))))
            case '-' | 'minus':
                print(text_linus + (rmatch[0] + ' - ' + rmatch[2] + ' = ' + str(float(rmatch[0]) - (float(rmatch[2])))))
            case '*' | 'x' | 'times':
                print(text_linus + (rmatch[0] + ' x ' + rmatch[2] + ' = ' + str(float(rmatch[0]) * (float(rmatch[2])))))
            case '/' | 'divided' | 'divided by':
                print(text_linus + (rmatch[0] + ' ÷ ' + rmatch[2] + ' = ' + str(float(rmatch[0]) / (float(rmatch[2])))))
            case '^' | 'to the power of' | 'exponent' | '**':
                print(text_linus + (rmatch[0] + '^' + rmatch[2] + ' = ' + str(float(rmatch[0]) ** (float(rmatch[2])))))
    return "Done!"

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
        "responses": ["I can answer your questions and provide information on various topics.", "I'm trained to have conversations and generate text based on the input I receive.", "I can help with tasks such as language translation, summarization, and many others."]
    },
    {
        "input": ["what do you like", "what's your favorite thing", "what do you enjoy"],
        "responses": ["As a language model, I don't have personal preferences or emotions.", "I don't have likes or dislikes, I just respond based on the input I receive."]
    },
    {
        "input": ["what is your favorite food", "whats your favorite food", "whats your favorite food to eat"],
        "reponse": ["I have never tried any!"]
    },
    {
        "input": ["what is your favorite number","whats your favorite number"],
        "response": ["My favorite number is 56!"]
    },
    {
        "input": ["bye", "goodbye", "see you later", "talk to you later"],
        "responses": ["Goodbye!", "Bye!", "See you later!", "Take care!"]
    },
    {
        "input" : ["linus"],
        "response": ["Yes?", "That's my name!"]
    },
    {
        "input": ["what can you do","what are your abilities", "what do you do","list what can you do","what features do you have"],
        "responses": abilities,
    },
    {
        "input": ["what is your name","whats your name","your name","who are you"],
        "responses": ["You can call me Linus","My name is Linus", "I'm Linus!","I'm Linus, how are you?"],
    },
    {
        "input": ["pong game", "play pong", "play pong game", "pong"],
        "action": "pongGame",
    },
    {
        "input": ["play tic tac toe","ttt","tic tac toe","tictactoe", "play tictactoe", "play ttt"],
        "action": "tic_tac_toe"
    },
    {
        "regex": r'(^play)\s*((the song)?)\s*([\w\s]*)',
        "action": "playSong",
    },
    {
        "regex": r'(\d*\.?\d+)\s*(\*|x|\/|\+|-|\^|\*\*|times|minus|plus|divide|divided by|to the power of|exponent)\s*(\d*\.?\d+)',
        "action": "mathing",
    },
    {
        "input": ["list the songs you can play", "list songs", "song list", 'list your songs', "list all songs","list the songs", "songs list", "give me a list of the songs you can play", 'list the songs you can play'],
        "action": "listTheSongs",
    },
    {
        "input": ["song request", "i want to request a song", "request song", 'songs request', "request a song", "make a song request", "add more songs", "add a song"],
        "action": "songRequests",
    },
    {
        # "regex": r'(capital|currency)\s*(?:of)?\s*(?:the)?\s*(.*)',
        "regex": r'^(?:(?!country).)*(capital|currency)\s*(?:of)?\s*(?:the)?\s*(.*)',
        "action": "countryData"
    },
    {
        "regex": r'(?:what country)\s*(?:has)?\s*(?:the)?\s*(capital|currency)\s*([\w\d\s]*)',
        "action": "countryDataReverse"
    },
    {
        "regex": r'(sin|cos|tan|sin-1|cos-1|tan-1|sine|cosine|tangent|sine-1|cosine-1|tangent-1)\s*(?:of)?\s*(\d*\.?\d+)',
        "action": "SinCosTan"
    }
]




defaultResponse = ["I'm sorry, I don't understand.","I'm not sure I follow?","I don't understand, make sure you spelled it right..."]

def chatbot_response(talk, untalk):
    for response in responses:
        if "regex" in response:
            regexMatches = re.findall(response['regex'], untalk)
            if regexMatches:
                if "action" in response:
                    func = globals()[response['action']]
                    return func(regexMatches)
                elif "responses" in response:  
                    return random.choice(response["responses"])

        elif talk in response['input']:
            if "action" in response:
                func = globals()[response['action']]
                return func()
            else:
                return random.choice(response["responses"])
        
    return random.choice(defaultResponse)
        

while True: 
    untalk = input(colored(">> ", 'red', attrs=['dark', 'bold'])).lower()
    if untalk.lower() == "!end":
        break
    if untalk.lower() == "?":
        print("If there is something wrong, try asking: 'add feedback'.")
    talk = re.sub(r'[^\w\s\d]', '', untalk)
    print(text_linus + chatbot_response(talk, untalk))
