import re
import os
from termcolor import colored
import time
import random
import pygame
from email.message import EmailMessage
import ssl
import smtplib
from TicTacToe2p import tic_tac_toe2p
from TicTacToe1p import tic_tac_toe1p



alphabet = ['a','b','c','d','e','f','g','h','i','j']

os.system('cls')
# region Welcoming
print('--------------------------------------------------------------------------')
print('Welcome To Linus 1.0, A Responding Terminal To Some Of Your Questions!')
print("Try Asking 'Hi' or 'What is your name'")
print('--------------------------------------------------------------------------')
print('\n')

# endregion

# https://regexr.com/

# Join with folder 'songs'
current_directory = os.getcwd()
folder1 = 'data'
os.chdir(os.path.join(current_directory, folder1))

# region Variables
end = '!end'
# endregion

# songs, put exact as in folder 'songs'
songs = ['bang.mp3', 'karma.mp3', 'the good part.mp3','just like you.mp3', 'paid my dues.mp3']


roasts = [
    "There Is Someone Out There For Everyone. For You, It's A Therapist.",
    "The Movie About Your Life Would Be Amazing! ...As A Cure For Insomnia",
    "You Are The Reason There Are Instructions On Shampoo Bottles",
    "I Really Want To Hit You... But I'm Against Animal Abuse",
    "Sorry, I Can't Think Of A Dumb Enough Insult For You To Understand.",
    "It's Hilarious How You Are Trying To Fit Your Entire Vocabulary Into One Sentence.",
    "If I Had To Pick An Animal To Describe You, I'd Apologize... To The Animal.",
    "You Are Like A Software Uptdate, Every Time I See You I Immediatly Think 'Not Now'.",
    "It Would Be A Great Day If You Used Glue-Stick Instead Of Chapstick.",
    "Everyone Is Allowed To Act Stupid Once, But You... You Are Abusing That Privilege.",
    "Earth Is Full, Go Home.",
    "Why Are You Rolling Your Eyes? Are You Looking For Your Brain?",
    "If I Don't Answer You The First Time, What Makes You Think I Will In The Next 25?",
    "You Don't Need To Worry About The Zombie Apocalypse, They Only Go For People With Brains.",
    "Every Time I Think You Can't Get Any Dumber, You Prove Me Wrong.",
    "Why Don't You Slip Into Something More Comfortable... Like A Coma.",
    "I'd Love To Help You Out, But My Policy is to Never Do Any Work Before Coffee.",
    "If Laughter Is The Best Medicine, Your Face Must Be Curing The World.",
    "I'm Sorry, I Don't Speak Idiot.",
    "I Can Explain It To You, But I Can't Understand It For You.",
]

twoPartJokes = [
    ['What do you call a dinosaur with a wide vocabulary?', 'A Thesaurus'],
    ['What do you call a fake noodle?', 'An Impasta'],
    ["Why did the teddy bear say no to dessert?", "Because He Was Stuffed!"],
    ["A Man Walked Into A Bar And What Did He Say?", 'ow'],
    ['You know why you never see elephants hiding up in trees?', 'Because They Are Really Good At It!'],
    ["What Is Red And Smells Like Blue Paint?", 'Red Paint'],
    ["Why aren't koalas actual bears?", "The don't meet the koalafications."],
    ["What do you call bears with no ears?", "B"],
    ["How do you make a tissue dance?", "You put a little boogie in it."],
    ["What do you call a train chewing bubblegum?", "A Chew-Chew Train."],
    ["What's a foot long and slippery?", "A slipper."],
    ["Two gold fish are in a tank. What does one say?", "Do You Know How To Drive This Thing?"],
    ["Why doesn't the sun go to college?", "Because it has a million degrees!"],
    ["As a scarecrow, people say I'm outstanding in my field.", "But hay it's in my jeans."],
    ["Why did the scarecrow win the talent show?", "Because he was outstanding in his field."],
    ["How did the hipster burn his mouth.", "Because he ate pizza before it was 'cool'."],
    [" I waited and stayed up all night and tried to figure out where the sun was.", "Then it dawned on me..."],
    ["What's red and moves up and down?", "A Tomatoe on an elevator."],
    ["Can February march?", "No, but April May."],
]

pattern = r'(\d*\.?\d+)\s*(\*|x|\/|\+|-|\^|\*\*|times|minus|plus|divide|divided by|to the power of|exponent)\s*(\d*\.?\d+)'
repeat = 0
def songRequest():
    #send email through python
    request = input('Enter A Song Request, Including Author, And Title (Enter Real Song!): ')

    #from 'who?'
    email_sender = 'linuschatbot@gmail.com'
    #code, do not share
    email_password = 'wtockzyhzehlrigl'
    #reciever (also forwarded to jstark09@nca.edu.ni, using filters in judahstarkenburg@gmail.com account)
    email_reciever = 'judahstarkenburg@gmail.com'

    #input the users email
    user_email = input("Enter YOUR Email To Recieve Further Information About The Song Request Made (Required!): ")
    
    #check if its a valid email adress, if it is, send it with body text and info
    if '@gmail.com' in user_email or '@yahoo.com' in user_email or '@nca.edu.ni' in user_email or '@hotmail.com' in user_email:
        subject = 'New Song Request!'
        body = ("""
        ----------------------
        Someone Has Requested For The Song: 
        """ + request + """
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
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())
            print("Song Request Made!")

    else:
        os.system('cls')
        print("Invalid Email!")
        time.sleep(1)
        songRequest()


while repeat == 0:

    untalked = input('>>  ')
    talk = (untalked.lower())
    regex = re.findall(pattern, talk)

    #-------------------------------This Was Mostly Done By Chat GPT
    if 'play' in talk:  
        for song in songs:
            if song[:-4].lower() in talk:
                pygame.init()
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                print("Playing "+ song[:-4])
                break
        #----------------------------
        #add song request
        else:
            print("We Don't Have That Song!")
            y_n = input("Would You Like To Make A Song Request?[y/n]: ")

            if 'y' in y_n:
                songRequest()

            elif 'n' in y_n:
                print('')

            else:
                print('')

    elif 'stop' in talk:
        pygame.mixer.music.stop()
        print("Song stopped.")


    elif 'pause' in talk:
        pygame.mixer.music.pause()
        print("Song paused.")

    elif '    ' in talk:
        print("you have to write something")


    elif 'resume' in talk:
        if pygame.mixer.get_init() == None:
            print("Mixer not initialized. Cannot resume music.")
        else:
            pygame.mixer.music.unpause()
            print("Song resumed.")


    elif ('list' in talk and 'songs' in talk) or ('songs' in talk) or ('song list' in talk):
        print("""
-------------------------------------------------
|Say           Action                           |
|-----------------------------------------------|
|(Play): Use "Play <Song>"                      |
|(Stop): Stops The Song                         |
|(Pause): Pauses The Song                       |
|(Resume): Needs To Be Paused, Resumes The Song |
|(Manual Song): Manually Add Song To List       |
|(Song Request): Make A Song Request            |
-------------------------------------------------
Songs:""")
        list_numbered = 0
        for i in range(len(songs)):
            list_numbered += 1
            print(str(list_numbered) + '. ' + songs[i][:-4])
    
    elif ('suggest' in talk and 'song' in talk) or ('song' in talk and 'request' in talk):
        songRequest()


    elif 'is your name' in talk:
        print('You can call me Linus!')

    elif 'manual' and 'song' in talk:
        y_n_manual_song = input("Would You Like To Manually Add A Song?[y/n]")
        if 'y' in y_n_manual_song:
            print("""
====================================================================================================================================
Five Rules:
1. Write The Song In The Format Of song.mp3 (No Caps!)
2. Only MP3 Files!
3. Add The Song FILE To The Data Folder.
4. Note: You WILL Need To Add The Song Name To The List Every Time You Open Linus, Thats Why It's Easier To Ask For A Song Request!
4. Make Sure The File You Added Is The EXACT Same As The Song You Add To This Input:
=================================================================================================================================== """)
            user_input = input("Enter a song to add to the list, Remember To Add '.mp3': ")
            print("New Song: '" + (user_input[:-4]).lower() + "' Added!")
            songs.append(user_input.lower())
        elif 'n' in y_n_manual_song:
            print()
        else:
            print()

    elif 'hello' in talk:
        print('Hello!')
    
    elif 'who' in talk and 'made' in talk and 'you' in talk:
        print("My Creators Are Judah Starkenburg, Micah Uhl, and Help From Chat GPT And Judah's Dad.")

    elif 'hi' in talk:
        print('Hi!')
    
    elif 'give' in talk and 'me' in talk and 'your' in talk and 'code' in talk:
        print("Can't Do That! :(")

    elif 'search' in talk and 'google' in talk:
        print("That Will Become A Feature In The Future, It's Not Accessible Right Now, Sorry!")


    elif 'your' in talk and 'favorite' in talk and 'color' in talk:
        print("My Favorite Color Is Orange, The Color Of A Sunset!")

    elif 'your' in talk and 'favorite' in talk and 'number' in talk:
        print("My Favorite Number is 56, It's The First Number That Comes To Mind!")

    elif 'your' in talk and 'favorite' in talk and 'food' in talk:
        print("I Haven't Tried Any!")

    elif 'tic' in talk and 'tac' in talk and 'toe' in talk:
        ttt_1_2 = int(input("Would You Like To Play 2 Player, Or 1 Player? [1/2/quit]: "))
        if ttt_1_2 == 2:
            tic_tac_toe2p()
        elif ttt_1_2 == 1:
            tic_tac_toe1p()

    elif 'roast' in talk:
        roast = random.randint(0, len(roasts) - 1)
        # roast20 = colored("I Can Explain It To You, But I Can't Understand It For You.", 'red', attrs=['dark', 'bold'])

        print(colored(roasts[roast], 'red', attrs=['dark', 'bold']))

    elif 'number' in talk and 'guessing' in talk and 'game' in talk:
        text1 = colored('You Must Guess 1-100!', 'yellow')
        text2 = colored(' -1 Guess', 'red', attrs=["dark", "bold"])
        text3 = colored('Guesses Left: ', 'blue', attrs=["dark", "bold"])
        text5 = colored('You Lose! The Number Was ', 'red', attrs=['dark', 'bold'])



        number = random.randrange(1,500)
        guesses = 0
        left = 8
        os.system('cls')
        print('Welcome To The Guessing Game, Guess The Number, In 8 Tries!')
        while guesses <= 8:
            guesses += 1
            left -= 1 
            text4 = colored(left, 'red')
            guess = float(input('Guess A Number 1-500: '))
            os.system('cls')
            print((colored('Your Last Guess Was: ', 'red')) + str(guess))
            if guess == number:
                print(colored('########', 'green'))
                print(colored('You Win!', 'yellow'))
                print(colored('########', 'green'))
                time.sleep(2)
                break
            if left == 0:
                answer = str(colored(number, 'green'))
                print(text5 + answer)
                time.sleep(2)
                break
            elif guess < number:
                print(colored('The Number Is Higher!', 'cyan'))
            elif guess > number:
                print(colored('The Number Is Lower!', 'cyan'))
            if guess > 500:
                print(text1 + text2)
            if guess < 0:
                print(text1 + text2)
            print(text3 + str(text4))

    elif 'game' in talk:
        print("Games: ")
        print("  Number Guessing Game")
        print("  1 Player Tic Tac Toe")
        print("  2 Player Tic Tac Toe")


    elif 'joke' in talk and 'tell' in talk:
        joke = random.randint(0,19)
        if joke < 19:
            thisJoke = twoPartJokes[joke]
            print(colored(thisJoke[0], 'blue', attrs=['bold','dark']))
            time.sleep(3)
            print(colored(thisJoke[1], 'blue'))
        elif joke == 19:
            print(colored("Here's a 3 Part Joke!:", 'blue', attrs=['bold','dark']))
            time.sleep(.5)
            print(colored("A guy goes into a lawyer's office and asks the lawyer: “Excuse me, how much do you charge?”", 'blue'))
            time.sleep(3)
            print(colored("£500 for 3 questions!", 'blue'))
            time.sleep(2)
            print(colored("That's a bit expensive, isn't it?", 'blue'))
            time.sleep(1.5)
            print(colored("Yes, Now whats your third question?", 'blue'))
    
    elif 'yay' in talk:
        print("Congrats!")

    elif regex:
        for rmatch in regex:
            match rmatch[1]:
                case '+' | 'plus':
                    print(rmatch[0] + ' + ' + rmatch[2] + ' = ' + str(float(rmatch[0]) + (float(rmatch[2]))))
                case '-' | 'minus':
                    print(rmatch[0] + ' - ' + rmatch[2] + ' = ' + str(float(rmatch[0]) - (float(rmatch[2]))))
                case '*' | 'x' | 'times':
                    print(rmatch[0] + ' x ' + rmatch[2] + ' = ' + str(float(rmatch[0]) * (float(rmatch[2]))))
                case '/' | 'divided' | 'divided by':
                    print(rmatch[0] + ' ÷ ' + rmatch[2] + ' = ' + str(float(rmatch[0]) / (float(rmatch[2]))))
                case '^' | 'to the power of' | 'exponent' | '**':
                    print(rmatch[0] + '^' + rmatch[2] + ' = ' + str(float(rmatch[0]) ** (float(rmatch[2]))))

    elif 'what are you' in talk:
        print('I am a Controlled Terminal Speech Creator, Sort Of Like An Ai, But Less Complex And Under Control!')

    elif end in talk:
        repeat = 1
    
    elif 'help' in talk or ('what' in talk and 'can' in talk and 'you' in talk and 'do' in talk):
        os.system('cls')
        print("Info")
        print("Linus Can Do Multiplication, Division, Adding, Subtracting, And Exponents. (With 2 Numbers)")
        print("There Are Also Games, and Songs, Try Asking 'Games', Or 'List Songs'")

    else:
        print("I'm Not Sure I Understand?")
