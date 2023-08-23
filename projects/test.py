import re

def split_phrase(phrase):
    lower_phrase = phrase.lower()  # Convert the phrase to lowercase for case insensitivity

    last_is_index = lower_phrase.rfind(" is ")
    last_are_index = lower_phrase.rfind(" are ")

    if last_is_index > last_are_index:
        separator = " is "
    else:
        separator = " are "

    last_separator_index = max(last_is_index, last_are_index)

    if last_separator_index != -1:
        first_part = re.sub(r"my", "", phrase[:last_separator_index], flags=re.IGNORECASE).strip()
        second_part = phrase[last_separator_index + len(separator):].strip()
        return first_part, second_part
    else:
        return None

# Test cases
phrase1 = "My name is Judah"
phrase2 = "My favorite animals are cats"
phrase3 = "Samuel is my friend"
phrase4 = "Cats are amazing pets"

result1 = split_phrase(phrase1)
result2 = split_phrase(phrase2)
result3 = split_phrase(phrase3)
result4 = split_phrase(phrase4)

print(result1)
print(result2)
print(result3)
print(result4)
