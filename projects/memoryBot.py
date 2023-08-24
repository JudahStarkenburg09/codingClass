# pip install requests
from termcolor import cprint, colored
import re
import requests

youText = colored('?: ', 'blue')

class Store:
    def __init__(self):
        self.url = "https://languagetool.org/api/v2/check"
        self.language = "en-US"  # Change this if needed

        self.newInput = ""
        self.category_patterns = {
            "name": ["my name is"],
            "age": ["i am"],
            "likes": ["i like"],
            "friend": ["friend is", "is my friend"],
            # Add more categories and corresponding patterns here
        }
        self.separator_patterns = {
            "is": [" is "],
            "are": [" are "],
            "am": [" am "]
        }

    def memoryEntry(self, newInput):
        self.newInput = newInput
        self.memory = self.extract_info(self.newInput)
        


        return self.memory

    def extract_info(self, phrase):
        lower_phrase = phrase.lower()

        for category, cat_patterns in self.category_patterns.items():
            for cat_pattern in cat_patterns:
                if cat_pattern in lower_phrase:
                    category_info = re.sub(cat_pattern, "", phrase, flags=re.IGNORECASE).strip()
                    info = re.sub(r'\b(am|i|my)\b', '', category_info, flags=re.IGNORECASE).strip()
                    info = info.replace("years old", "").strip()
                    if category == 'friend':
                        category = 'friend'
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
    newInput = input(youText)
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
    print(response)
