import os

os.system('cls')
user_input = input('Enter Name: ')
email_input = input("Enter Email: ")

if 'gmail.com' in email_input or 'yahoo.com' in email_input or 'hotmail.com' in email_input or 'nca.edu.ni' in email_input:
    os.system('cls')
    print("Valid Email")
    print('----------------')
    print("Welcome " + user_input)
    print("User Information: ")
    print(user_input + ', Contact at: ' + email_input)

else:
    print("Invalid Email")

print('-----------------')