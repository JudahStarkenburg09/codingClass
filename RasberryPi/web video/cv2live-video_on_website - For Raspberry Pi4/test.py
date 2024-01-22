file_name = "email.txt"  # replace with your actual file name

with open(file_name, 'r') as file:
    email = file.readlines()

# Now 'email' is a list where each item corresponds to a line in the text file
print(email)
