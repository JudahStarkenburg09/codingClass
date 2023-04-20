import tkinter as tk
from termcolor import colored
import re
import random
import os
import pygame
import math
import time
from email.message import EmailMessage
import ssl
import smtplib
from mtranslate import translate
from langdetect import detect

languagesPrefixes= [
  {
    "prefix": "af",
    "name": "Afrikaans"
  },
  {
    "prefix": "sq",
    "name": "Albanian"
  },
  {
    "prefix": "am",
    "name": "Amharic"
  },
  {
    "prefix": "ar",
    "name": "Arabic"
  },
  {
    "prefix": "hy",
    "name": "Armenian"
  },
  {
    "prefix": "az",
    "name": "Azerbaijani"
  },
  {
    "prefix": "eu",
    "name": "Basque"
  },
  {
    "prefix": "be",
    "name": "Belarusian"
  },
  {
    "prefix": "bn",
    "name": "Bengali"
  },
  {
    "prefix": "bs",
    "name": "Bosnian"
  },
  {
    "prefix": "bg",
    "name": "Bulgarian"
  },
  {
    "prefix": "ca",
    "name": "Catalan"
  },
  {
    "prefix": "ceb",
    "name": "Cebuano"
  },
  {
    "prefix": "ny",
    "name": "Chichewa"
  },
  {
    "prefix": "zh-cn",
    "name": "Chinese (Simplified)"
  },
  {
    "prefix": "zh-tw",
    "name": "Chinese (Traditional)"
  },
  {
    "prefix": "co",
    "name": "Corsican"
  },
  {
    "prefix": "hr",
    "name": "Croatian"
  },
  {
    "prefix": "cs",
    "name": "Czech"
  },
  {
    "prefix": "da",
    "name": "Danish"
  },
  {
    "prefix": "nl",
    "name": "Dutch"
  },
  {
    "prefix": "en",
    "name": "English"
  },
  {
    "prefix": "eo",
    "name": "Esperanto"
  },
  {
    "prefix": "et",
    "name": "Estonian"
  },
  {
    "prefix": "tl",
    "name": "Filipino"
  },
  {
    "prefix": "fi",
    "name": "Finnish"
  },
  {
    "prefix": "fr",
    "name": "French"
  },
  {
    "prefix": "fy",
    "name": "Frisian"
  },
  {
    "prefix": "gl",
    "name": "Galician"
  },
  {
    "prefix": "ka",
    "name": "Georgian"
  },
  {
    "prefix": "de",
    "name": "German"
  },
  {
    "prefix": "el",
    "name": "Greek"
  },
  {
    "prefix": "gu",
    "name": "Gujarati"
  },
  {
    "prefix": "ht",
    "name": "Haitian Creole"
  },
  {
    "prefix": "ha",
    "name": "Hausa"
  },
  {
    "prefix": "haw",
    "name": "Hawaiian"
  },
  {
    "prefix": "iw",
    "name": "Hebrew"
  },
  {
    "prefix": "he",
    "name": "Hebrew"
  },
  {
    "prefix": "hi",
    "name": "Hindi"
  },
  {
    "prefix": "hmn",
    "name": "Hmong"
  },
  {
    "prefix": "hu",
    "name": "Hungarian"
  },
  {
    "prefix": "is",
    "name": "Icelandic"
  },
  {
    "prefix": "ig",
    "name": "Igbo"
  },
  {
    "prefix": "id",
    "name": "Indonesian"
  },
  {
    "prefix": "ga",
    "name": "Irish"
  },
  {
    "prefix": "it",
    "name": "Italian"
  },
  {
    "prefix": "ja",
    "name": "Japanese"
  },
  {
    "prefix": "jw",
    "name": "Javanese"
  },
  {
    "prefix": "kn",
    "name": "Kannada"
  },
  {
    "prefix": "kk",
    "name": "Kazakh"
  },
  {
    "prefix": "km",
    "name": "Khmer"
  },
  {
    "prefix": "rw",
    "name": "Kinyarwanda"
  },
  {
    "prefix": "ko",
    "name": "Korean"
  },
  {
    "prefix": "ku",
    "name": "Kurdish (Kurmanji)"
  },
  {
    "prefix": "ky",
    "name": "Kyrgyz"
  },
  {
    "prefix": "lo",
    "name": "Lao"
  },
  {
    "prefix": "la",
    "name": "Latin"
  },
  {
    "prefix": "lv",
    "name": "Latvian"
  },
  {
    "prefix": "lt",
    "name": "Lithuanian"
  },
  {
    "prefix": "lb",
    "name": "Luxembourgish"
  },
  {
    "prefix": "mk",
    "name": "Macedonian"
  },
  {
    "prefix": "mg",
    "name": "Malagasy"
  },
  {
    "prefix": "ms",
    "name": "Malay"
  },
  {
    "prefix": "ml",
    "name": "Malayalam"
  },
  {
    "prefix": "mt",
    "name": "Maltese"
  },
  {
    "prefix": "mi",
    "name": "Maori"
  },
  {
    "prefix": "mr",
    "name": "Marathi"
  },
  {
    "prefix": "mn",
    "name": "Mongolian"
  },
  {
    "prefix": "my",
    "name": "Myanmar (Burmese)"
  },
  {
    "prefix": "ne",
    "name": "Nepali"
  },
  {
    "prefix": "no",
    "name": "Norwegian"
  },
  {
    "prefix": "or",
    "name": "Odia"
  },
  {
    "prefix": "ps",
    "name": "Pashto"
  },
  {
    "prefix": "fa",
    "name": "Persian"
  },
  {
    "prefix": "pl",
    "name": "Polish"
  },
  {
    "prefix": "pt",
    "name": "Portuguese"
  },
  {
    "prefix": "pa",
    "name": "Punjabi"
  },
  {
    "prefix": "ro",
    "name": "Romanian"
  },
  {
    "prefix": "ru",
    "name": "Russian"
  },
  {
    "prefix": "sm",
    "name": "Samoan"
  },
  {
    "prefix": "gd",
    "name": "Scots Gaelic"
  },
  {
    "prefix": "sr",
    "name": "Serbian"
  },
  {
    "prefix": "st",
    "name": "Sesotho"
  },
  {
    "prefix": "sn",
    "name": "Shona"
  },
  {
    "prefix": "sd",
    "name": "Sindhi"
  },
  {
    "prefix": "si",
    "name": "Sinhala"
  },
  {
    "prefix": "sk",
    "name": "Slovak"
  },
  {
    "prefix": "sl",
    "name": "Slovenian"
  },
  {
    "prefix": "so",
    "name": "Somali"
  },
  {
    "prefix": "es",
    "name": "Spanish"
  },
  {
    "prefix": "su",
    "name": "Sundanese"
  },
  {
    "prefix": "sw",
    "name": "Swahili"
  },
  {
    "prefix": "sv",
    "name": "Swedish"
  },
  {
    "prefix": "tg",
    "name": "Tajik"
  },
  {
    "prefix": "ta",
    "name": "Tamil"
  },
  {
    "prefix": "tt",
    "name": "Tatar"
  },
  {
    "prefix": "te",
    "name": "Telugu"
  },
  {
    "prefix": "th",
    "name": "Thai"
  },
  {
    "prefix": "tr",
    "name": "Turkish"
  },
  {
    "prefix": "tk",
    "name": "Turkmen"
  },
  {
    "prefix": "uk",
    "name": "Ukrainian"
  },
  {
    "prefix": "ur",
    "name": "Urdu"
  },
  {
    "prefix": "ug",
    "name": "Uyghur"
  },
  {
    "prefix": "uz",
    "name": "Uzbek"
  },
  {
    "prefix": "vi",
    "name": "Vietnamese"
  },
  {
    "prefix": "cy",
    "name": "Welsh"
  },
  {
    "prefix": "xh",
    "name": "Xhosa"
  },
  {
    "prefix": "yi",
    "name": "Yiddish"
  },
  {
    "prefix": "yo",
    "name": "Yoruba"
  },
  {
    "prefix": "zu",
    "name": "Zulu"
  }
]

allRoasts = [
    {
        "roast": "I'd call you a tool, but that would be an insult to useful things."
    },
    {
        "roast": "If you were any more inbred, you'd be a sandwich."
    },
    {
        "roast": "I'd tell you to go outside and get some fresh air, but I don't want you to breath."
    },
    {
        "roast": "Your birth certificate is an apology letter from the hospital."
    },
    {
        "roast": "The only thing you're faster than is a freaking glacier."
    },
    {
        "roast": "I'd roast you, but my mom said I'm not allowed to burn trash."
    },
    {
        "roast": "I'm not insulting you, I'm describing you."
    },
    {
        "roast": "You're so ugly, when you were born, the doctor slapped your mother."
    },
    {
        "roast": "You're the reason the gene pool needs a lifeguard."
    },
    {
        "roast": "I'm surprised you haven't tripped over that massive ego of yours yet."
    },
    {
        "roast": "You're like a dictionary, you add meaning to my life, but only a little bit."
    },
    {
        "roast": "I'd roast you, but you look like you've already been burned enough."
    },
    {
        "roast": "I'm sorry, I didn't mean to make you cry. I meant to make you ugly-cry."
    },
    {
        "roast": "You're the human equivalent of a participation award."
    },
    {
        "roast": "I bet your parents change the subject when their friends ask about you."
    },
    {
        "roast": "I'm not saying I hate you, but I would unplug your life support to charge my phone."
    },
    {
        "roast": "You're like the top piece of bread in a loaf, everybody touches you but nobody wants you."
    },
    {
        "roast": "Your face looks like it was on fire and someone put it out with a fork."
    },
    {
        "roast": "You're about as useful as a screen door on a submarine."
    },
    {
        "roast": "Your face is so oily, I'm surprised America hasn't declared war on it yet."
    },
    {
        "roast": "I'd insult you, but I don't want to give you any material for your next rap battle."
    },
    {
        "roast": "You're the reason they invented double doors."
    },
    {
        "roast": "If your IQ was any lower, we'd have to water you twice a week."
    },
    {
        "roast": "Your face looks like you've been using it as a punching bag."
    }
]

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

def newQuestionAsked(question):
    email_sender = 'linuschatbot@gmail.com'
    #code, do not share
    email_password = 'wtockzyhzehlrigl'
    #reciever (also forwarded to jstark09@nca.edu.ni, using filters in judahstarkenburg@gmail.com account)
    email_reciever = 'judahstarkenburg@gmail.com'

    
    #check if its a valid email adress, if it is, send it with body text and info
    subject = '<Linus> New Possible Question To Add!'
    body = ("""
    ----------------------
    Someone Has Asked: 
    """ + question + """
    ----------------------
    And There Was No Response!
    """)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    thecontext = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=thecontext) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

    return


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

def chooseRoast():
    roast = random.choice(allRoasts)
    return roast["roast"]

def chooseJoke():
    joke = random.choice(allJokes)
    return [joke["joke"], joke["secondResponse"]]

responses = [
    {
        "input": ['hi','hello','sup',"wassup","hey","whats up",'hi linus','hello linus','sup linus',"wassup linus","hey linus","whats up linus"], #Never put capital letters or punctuation inside "input", Also make sure to add many options
        "responses": ["Hello!", "Hi there!", "Hey!", "Hi!"], #Use correct grammer, with multiple responses. Try not to add many questions, but if you do, than make sure to add a new "input" with what the user would answer with
    },
    {
        "input": ['yes', 'ya'],
        "responses": ['good']
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
        "responses": ["I can do math, tell jokes, and even roast you!"]
    },
    {
        "input": ["what do you like", "what's your favorite thing", "what do you enjoy"],
        "responses": ["As a chatbot, I don't have personal preferences or emotions.", "I don't have likes or dislikes, I just respond based on the input I receive."],
    },
    {
        "input": ["what is your favorite food", "whats your favorite food", "whats your favorite food to eat"],
        "reponses": ["I have never tried any!"],
    },
    {
        "input": ["what is your favorite number","whats your favorite number"],
        "responses": ["My favorite number is 56!"],
    },
    {
        "input": ["bye", "goodbye", "see you later", "talk to you later"],
        "responses": ["Goodbye!", "Bye!", "See you later!", "Take care!"],
    },
    {
        "input": ['ha', 'ah', 'haha', 'ahah', 'hahaha', 'ahahaha'],
        "responses": ["Very funny, isn't it?"]
    },
    {
        "input" : ["linus"],
        "responses": ["Yes?", "That's my name!"],
    },
    {
        "input": ['tell me a joke', 'joke', 'tell me another joke', "tell joke", "another joke", "tell me a joke please", "another joke please"],
        "action": 'chooseJoke',
    },
    {
        "input": ["what is your name","whats your name","your name","who are you"],
        "responses": ["You can call me Linus","My name is Linus", "I'm Linus!","I'm Linus, how are you?"],
    },
    {
        "input": ["roast me", "give me a roast", "another roast", "roast", "roast me again"],
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
    
    newQuestionAsked(message)
    return random.choice(defaultResponse)
        
def send_jokePt2(response):
    history_text.yview(tk.END)
    history_text.insert('end', f'{response[1]} \n \n', ('response'))
    history_text.configure(state='disabled')
    return


def send_message():
    global response, message, respondWith
    message = input_text.get()
    untalk = message.lower()
    talk = re.sub(r'[^\w\d]', '', untalk)
    history_text.yview(tk.END)

    prefix = detect(untalk)
    for l in languagesPrefixes:
        if l["prefix"] == prefix:
            language = l["name"]
    

    response = chatbot_response(talk, untalk)
    if '[' in str(response):
        history_text.configure(state='normal')
        history_text.insert('end', 'You: ')
        history_text.insert('end', message + '\n', ('user'))
        history_text.insert('end', 'Linus: ')
        history_text.insert('end', f'{response[0]}...   ', ('response'))
        history_text.yview(tk.END)
        history_text.after(2000, lambda: send_jokePt2(response))
        
        input_text.delete(0, tk.END)
    else:
        history_text.configure(state='normal')
        history_text.insert('end', 'You: ')
        history_text.insert('end', message + '\n', ('user'))
        history_text.yview(tk.END)
        history_text.insert('end', 'Linus: ')
        history_text.insert('end', f'{response} \n \n', ('response'))
        history_text.configure(state='disabled')
        input_text.delete(0, tk.END)
    history_text.yview(tk.END)
        




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
