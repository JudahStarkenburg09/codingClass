# pip install requests
from termcolor import cprint, colored
import re
import requests
import datetime

youText = colored('?: ', 'blue')

class Store:
    def __init__(self):
        self.url = "https://languagetool.org/api/v2/check"
        self.language = "en-US"  # Change this if needed
        self.memoryBank = []
        self.newInput = ""
        self.categoriesWithMatches = {"category": "likes", "responseCat": "likes",
                                       "category": "has", "responseCat": "has", }
        self.category_patterns = {
            "name": ["my name is"],
            "age": ["i am"],
            "likes": ["i like"],
            "friend": ["friend is", "is my friend"],
            "dad": ["is my dad", "my dad is", "my dads name is"],
            "mom": ["is my mom", "my mom is", "my moms name is"],
            "brother": ["is my brother", "my brother is", "my brothers name is"],
            "sister": ["is my sister", "my sister is", "my sisters name is"],
            "sibling": ["is my sibling", "my sibling is ", "my siblings name is"],
            "has": ["have"]
            # Add more categories and corresponding patterns here
        }
        self.separator_patterns = {
            "is": [" is "],
            "are": [" are "],
            "am": [" am "],
            "has": [" have "]
        }

    def memoryEntry(self, newInput):
        self.newInput = newInput
        self.memory = self.extract_info(self.newInput)
        self.current_time = datetime.datetime.now()
        self.formatted_time = f"{self.current_time.year}/{self.current_time.month}/{self.current_time.day} {self.current_time.hour}:{self.current_time.minute}:{self.current_time.second}"
        if not self.memory == None:
            print(self.memory)
            mt, m = self.memory
            print(mt)
            print(m)
            self.memoryToAdd = {
                "type": f"{mt}",
                "memory": f"{m}",
                "timestamp": f"{self.formatted_time}",
            }
            self.memoryBank.append(self.memoryToAdd)
            print(self.memoryBank)
            return self.memory
        else:
            return self.memory
        
    def find_closest_memory(self, groupCheck):
        if not self.memoryBank:
            print("Memory bank is empty.")
            return None

        current_time = datetime.datetime.now()
        closest_memory = None
        closest_time_difference = float('inf')  # Initialize with a very large value

        for memory_entry in self.memoryBank:
            if memory_entry['type'] == groupCheck:
                entry_timestamp = datetime.datetime.strptime(memory_entry['timestamp'], '%Y/%m/%d %H:%M:%S')
                time_difference = abs((current_time - entry_timestamp).total_seconds())

                if time_difference < closest_time_difference:
                    closest_time_difference = time_difference
                    closest_memory = memory_entry

        if closest_memory:
            return closest_memory
        else:
            return f"No memories with group {groupCheck}"

    def extract_info(self, phrase):
        lower_phrase = phrase.lower()
        lower_phrase = re.sub(r"[^\w\d\s]", "", lower_phrase)
        for category, cat_patterns in self.category_patterns.items():
            for cat_pattern in cat_patterns:
                if cat_pattern in lower_phrase:
                    category_info = re.sub(cat_pattern, "", phrase, flags=re.IGNORECASE).strip()
                    info = re.sub(r'\b(am|i|my)\b', '', category_info, flags=re.IGNORECASE).strip()
                    info = info.replace("years old", "").strip()
                    if category == 'friend':
                        category = 'friend'
                    elif category == "dad":
                        category = "dad"
                    elif category == "mom":
                        category = 'mom'
                    elif category == 'has':
                        category = 'has'
                    elif category == 'brother':
                        category = 'brother'
                    elif category == 'sister':
                        category = 'sister'
                    elif category == 'sibling':
                        category = 'sibling'
                    elif category == 'likes':
                        category = 'likes'
                    elif category == "name":
                        return category, info
                    elif self.contains_integer_or_number_word(info):
                        category = "age"
                    elif category == "age" and self.contains_integer(info):
                        category = "age"
                    else:
                        category = "is" if category == "age" else "are"
                    if info.lower() == "i" and "i " in category_info:
                        category = "is"
                        info = info.replace("i", "").strip()
                    
                    return category, info
        return None
    
    def correct_grammar(self, textToChange):
        data = {
            "text": textToChange,
            "language": self.language,
        }
        
        response = requests.post(self.url, data=data)
        results = response.json()
        
        corrected_text = textToChange
        
        for match in reversed(results['matches']):
            replacements = match.get('replacements', [])
            if replacements:
                corrected_text = (
                    corrected_text[:match['offset']] +
                    replacements[0]['value'] +
                    corrected_text[match['offset'] + match['length']:]
                )
        
        return corrected_text

    def contains_integer_or_number_word(self, text):
        number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
        return any(char.isdigit() for char in text) or any(word in text for word in number_words)

    def remove_standalone_words(self, text, words):
        for word in words:
            text = re.sub(r'\b' + re.escape(word) + r'\b', '', text, flags=re.IGNORECASE).strip()
        return text

    def contains_integer(self, text):
        return any(char.isdigit() for char in text)

thoughts = Store()
while True:
    while True:
        newInput = input(youText)
        newInput = re.sub(r"[^\w\d\s]", "", newInput)
        if newInput.strip() == "":
            print("No input provided.")
            continue
        
        infoReceived = thoughts.memoryEntry(newInput)
        if infoReceived:
            category, info = infoReceived
            response = f"('{category}', '{info}')"
            response = re.sub(r"\b(i)\b", '', response, flags=re.IGNORECASE)
        else:
            response = "No matching pattern found."
        # print(response)

        if 'y' in input("y/n: "):
            break

    textToRespondForTest = thoughts.find_closest_memory(input("Check for closest group: "))
    print(textToRespondForTest)


