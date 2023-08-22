import re
import random
import time
from termcolor import cprint, colored


memoryRegex = '^(i am|my name is|i like)(.*)$'

class BotBrain:
    global botText, userInput, memoryRegex
    def __init__(self):
        self.responsesInputs = [
            {
                "input": "^(hello|hi|hi there|what's up|sup)$",
                "response": ["Hello!", "Hi there!"],
            },
            {
                "input": f"{memoryRegex}",
                "action": "storeMemory",
            },
            {
                "input": "^(how are you|how's it going|how are you doing)$",
                "response": ["I'm doing well, thank you!", "I'm here and ready to help!"],
            },
            {
                "input": "^(bye|goodbye|see you later|farewell)$",
                "response": ["Goodbye!", "Take care!"],
            },
            {
                "input": "^(tell me a joke|say something funny)$",
                "action": "runJokes",
            },
            # Add more regular expressions and responses/actions here
        ]

        self.allJokes = [
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
    
        self.memory = []  # List to store user inputs and memories
    
    def saveNewMemory(self, user_input, Newmemory, typeMemory):
        memory_entry = {
            "type": typeMemory,  # Replace with the appropriate type
            "mem": Newmemory,
        }
        self.memory.append(memory_entry)
        print(self.memory)

    def storeMemory(self, user_input):
        groups = re.search(f'{memoryRegex}', user_input)
        Newmemory = groups.group(1)
        typeMemory = groups.group(0)
        print(Newmemory)
        print(typeMemory)
        bot.saveNewMemory(user_input, Newmemory, typeMemory)

    def get_matching_response(self, user_input):
        for item in self.responsesInputs:
            if re.match(item["input"], user_input, re.IGNORECASE):
                if "response" in item:
                    return item["response"]
                elif "action" in item:
                    func = getattr(self,item['action'])
                    return func(user_input)
        return None

    def process_input(self, user_input):
        response = self.get_matching_response(user_input)
        if not None:
            if isinstance(response, list):
                return response[0]
            elif callable(response):
                return response(user_input)
            else:
                return "I'm sorry, I didn't understand that."

    def runJokes(self, user_input):
        selected_joke = random.choice(self.allJokes)
        joke_setup = selected_joke["joke"]
        joke_punchline = selected_joke["secondResponse"]
        
        print(botText, joke_setup)
        time.sleep(2)  # Pause for 2 seconds
        print(joke_punchline)
        return None

# Creating an instance of the BotBrain class
bot = BotBrain()

botText = colored("Bot: ", 'red')

while True:
    yourInput = input(colored("You: ", 'blue'))
    if yourInput.lower() == "exit":
        print(f"{botText}Goodbye!")
        break
    botResponse = bot.process_input(yourInput)
    print(botText, botResponse)