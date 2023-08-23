from termcolor import cprint, colored
import re

youText = colored('?: ', 'blue')

class Store:
    def __init__(self):
        self.newInput = ""
        self.category_patterns = {
            "name": ["name is", "my name is"],
            "age": ["i am", "am"],
            "friend": ["friend is"],
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

        for separator, patterns in self.separator_patterns.items():
            for pattern in patterns:
                if pattern in lower_phrase:
                    category_info = re.sub(pattern, f"{separator} ", phrase, flags=re.IGNORECASE).strip()
                    for category, cat_patterns in self.category_patterns.items():
                        for cat_pattern in cat_patterns:
                            if cat_pattern in category_info:
                                info = re.sub(cat_pattern, "", category_info, flags=re.IGNORECASE).strip()
                                if category == "age":
                                    if self.contains_integer(info):
                                        info = re.sub(r'\b(am|i)\b', '', info, flags=re.IGNORECASE).strip()
                                    else:
                                        category = "is"
                                else:
                                    info = re.sub(r'\b(am|i)\b', '', info, flags=re.IGNORECASE).strip()
                                info = info.replace("years old", "").strip()
                                if info.lower() == "i" and "i " in category_info:
                                    category = "is"
                                    info = info.replace("i", "").strip()
                                return category, info
        return None

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
