import json

# Emoji array for profiles
profiles = [
    {"name": "smile", "emoji": "😀"},
    {"name": "sunglasses", "emoji": "😎"},
    {"name": "starry", "emoji": "🤩"},
    {"name": "sad", "emoji": "😟"},
    {"name": "angry", "emoji": "😡"}
]

# File path where you want to save the JSON file
file_path = "profiles.json"

# Function to encode emojis to UTF-8
def encode_emojis(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8').decode('utf-8')
    return obj

# Write the profiles array to the JSON file
with open(file_path, "w", encoding='utf-8') as json_file:
    json.dump(profiles, json_file, indent=4, ensure_ascii=False, default=encode_emojis)

print("JSON file has been created successfully.")
