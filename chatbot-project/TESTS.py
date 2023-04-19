import translate

# Define the function to handle user input
def handle_user_input(input_text):
    # Detect the language of the input
    language = translate.detect(input_text)

    # Translate the input to English if it's not already in English
    if language != 'en':
        translation = translate.translate(input_text, dest='en')
        input_text = translation.text

    return input_text, language

# Example usage
input_text = "hola"
output_text, language = handle_user_input(input_text)
print(f"Input text: {input_text}")
print(f"Detected language: {language}")
print(f"Translated text: {output_text}")
