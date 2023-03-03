import random
from termcolor import colored
import os
import time
os.system('cls')
text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])
print(text_linus + "Please wait...")
import nltk
progressBar = [colored('[█   ]', 'green'), colored('[██  ]', 'green'), colored('[███ ]', 'green'), colored('[████]', 'green')]
if not nltk.downloader.Downloader().is_installed('wordnet'):
    print(text_linus + "Downloading 'wordnet' corpus, a useful feature for this app... Please do not close the application, it will be a short download!")
    nltk.download('wordnet', quiet=False)
    for i in range(4):
        os.system('cls')
        print(progressBar[i])
        time.sleep(0.33333)

    
    




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
from nameGenerator import randName
from gaunteloco import guanteloco
import math
from hangman import hangManGame
from carGameForChatbot import carGame
from receiptProjectPDF import receiptPrank
from jokesDatabase import allJokes
from roastDatabase import allRoasts
os.system("cls")

os.system('cls')

abilities = ["""
I can do many things, some things I can do are:
> list songs
Math (ex. 5*5, 8^3, 9/4)
Games (ex. pong, tic tac toe, hangman, name generator, car game)
> 
"""]

listGames = ["""
Hangman
Tic Tac Toe
Pong
Name Generator
Car Game
"""]


def stopSong():
    if pygame.mixer.get_init() == None:
        return "No songs to stop!"
    else:
        pygame.mixer.music.pause()
        return "Song stopped"

def pauseSong():
    if pygame.mixer.get_init() == None:
        return "No songs to pause!"
    else:
        pygame.mixer.music.pause()
        return "Music paused!"
    
def resumeSong():
    if pygame.mixer.get_init() == None:
        return "No music to resume"
    else:
        pygame.mixer.music.unpause()
        return "Song resumed"
    

def restartSong():
    if pygame.mixer.get_init() == None:
        return "No music to restart"
    else:
        pygame.mixer.music.stop()
        pygame.mixer.music.play()
        return "Song restarted"

def fakeReceipt():
    return receiptPrank()

def responseHello(regexMatches, talk):
    helloResponseComplexList = [f"Hello {regexMatches[0]}, I'm Linus!", f"Hello {regexMatches[0]}, my name is Linus!", f"Hi {regexMatches[0]}, I'm Linus!"]
    helloChoiceResponse = random.choice(helloResponseComplexList)
    return helloChoiceResponse

def tic_tac_toe():
    tictactoe1_2 = input(text_linus + "Would you like to play tic tac toe 1 player or 2 player? [1/2/quit]: ")
    if '1' in tictactoe1_2:
        return tic_tac_toe1p()
    elif '2' in tictactoe1_2:
        return tic_tac_toe2p()
        
    else:
        return "Canceled"

def randomNameGenerator():
    return randName()

def guanteLocoGame():
    return guanteloco()

def playHangMan():
    return hangManGame()

current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

text_linus = colored('<Linus> ', 'green', attrs=['dark','bold'])

songList = ["bang.mp3","just like you.mp3","karma.mp3","paid my dues.mp3","the good part.mp3"]

def countryDataReverse(pattern, talk):
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

def countryData(pattern, talk):
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



def playSong(pattern, talk):
    patternSongPlaying = pattern[0][3]
    pygame.init()
    if (patternSongPlaying + '.mp3') in songList:
        pygame.mixer.music.load(patternSongPlaying + '.mp3')
        pygame.mixer.music.play()
        return ("Playing " + patternSongPlaying)
    else:
        return "We don't have that song! Try asking 'song request'."

def listTheSongs():
    os.system('cls')
    print("Songs you can play: ")
    for i, song in enumerate(songList, start=1):
        print(colored(f"{i}. ", 'red', attrs=['bold','dark']) + song[:-4])
    return """
Say 'play' + song, to play a song!
Say 'pause', to pause the song!
Say 'resume', to continue the song!
say 'stop', to stop the song!


"""

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
    
def chooseJoke():
    joke = random.choice(allJokes)
    print(text_linus + joke["joke"])
    time.sleep(3)
    return joke["secondResponse"]

def chooseRoast():
    roast = random.choice(allRoasts)
    return roast["roast"]


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

def carHighwayGame():
    carGame()


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
        "responses": abilities,
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
        "action": "tic_tac_toe",
    },
    {
        "input": ["play guanteloco", "play baseball game", "play guanteloco game", "play baseball", "guanteloco", "baseball", "guanteloco game", "baseball game"],
        "action": 'guanteLocoGame',
    },
    {
        "input": ['hangman', 'play hangman', 'hangman game', 'play hangman game'],
        "action": 'playHangMan',
    },
    {
        "input": ["pick a random name", "random name", "random name generator", "play name generator" "play name generator game"],
        "action": "randomNameGenerator",
    },
    {
        "input": ["roast me", "give me a roast", "another roast", "roast"],
        "action": 'chooseRoast',
    },
    {
        "input": ["testapplication"],
        "action": "fakeReceipt",
    },
    {
        "input": ["stop", "stop playing", "stop song"],
        "action": 'stopSong',
    },
    {
        "input": ["pause", "pause playing", "pause song"],
        "action": 'pauseSong',
    },
    {
        "input": ["resume", "resume song", "resume playing", "continue song", "continue playing", "continue"],
        "action": 'resumeSong',
    },
    {
        "input": ["play", "play song"],
        "action": 'resumeSong',
    },
    {
        "input": ["play", "play song"],
        "action": 'resumeSong',
    },
    {
        "input": ["restart", "restart song", "start over", "play again"],
        "action": "restartSong",
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
        "input": ["list games", "games", "what games do you have", "what games are there", "list your games", "list the games you have", "list the games"],
        "responses": listGames,
    },
    {
        "regex": r'(\d*\.?\d+)\s*(\*|x|\/|\+|-|\^|\*\*|times|minus|plus|divide|divided by|to the power of|exponent)\s*(\d*\.?\d+)',
        "action": "mathing",
    },
    {
        "input": ['play car game', 'car game', 'play the car game', 'cargame'],
        "action": 'carHighwayGame'
    },
    {
        # "regex": r'(capital|currency)\s*(?:of)?\s*(?:the)?\s*(.*)',
        "regex": r'^(?:(?!country).)*(capital|currency)\s*(?:of)?\s*(?:the)?\s*(.*)',
        "action": "countryData",
    },
    {
        "regex": r'(?:what country)\s*(?:has)?\s*(?:the)?\s*(capital|currency)\s*([\w\d\s]*)',
        "action": "countryDataReverse",
    },
    {
        "regex": r'(sin|cos|tan|sin-1|cos-1|tan-1|sine|cosine|tangent|sine-1|cosine-1|tangent-1)\s*(?:of)?\s*(\d*\.?\d+)',
        "action": "SinCosTan",
    },
    {
        "regex": r'^(?:hi|hello)?\s*(?:,|\.)*\s*(?:linus)?\s*(?:,|\.)*\s*(?:im|my names|my name is)\s*(\w*\s*)',
        "action": 'responseHello', 
    },
    {
        "regex": r'(^play)\s*((the song)?(?:song)?)\s*([\w\s]*)',
        "action": "playSong",
    },
]




defaultResponse = ["I'm sorry, I don't understand.","I'm not sure I follow?","I don't understand, make sure you spelled it right..."]

def chatbot_response(talk, untalk):
    for response in responses:
        if "regex" in response:
            regexMatches = re.findall(response['regex'], untalk) 
            if regexMatches:
                if "action" in response:
                    func = globals()[response['action']]
                    return func(regexMatches, talk)
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
