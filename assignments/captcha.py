import string
import random
import captcha

# Define the length of the CAPTCHA
length = 6

# Define the characters used for the CAPTCHA
characters = string.ascii_letters + string.digits

# Generate a random CAPTCHA image and string
image, captcha_text = captcha.image.generate(length=length, chars=characters)

# Display the CAPTCHA image
image.show()

# Ask the user to enter the CAPTCHA
answer = input('Enter the CAPTCHA: ')

# Check if the user's answer matches the CAPTCHA
if answer == captcha_text:
    print('Success! You are human.')
else:
    print('Sorry, that was incorrect. Please try again.')
