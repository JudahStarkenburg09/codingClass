def colored_input(prompt, color_code):
    return input(f"\033[{color_code}m{prompt}\033[0m")

color_code = "31"  # Red color code
user_input = colored_input("Enter your text: ", color_code)
print("You entered:", user_input)
