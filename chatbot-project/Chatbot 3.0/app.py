from responses import responses
import re
import random
from termcolor import colored, cprint

class Main:
    def __init__(self):
        self.responses = responses

    def get_response(self, user_input):
        for response_set in self.responses:
            for pattern in response_set["in"]:
                if re.match(pattern, user_input):
                    return random.choice(response_set["out"])
        return "I'm sorry, I don't understand."

# Example of usage
if __name__ == "__main__":
    main_instance = Main()

    while True:
        user_input = input(f"{colored('You: ', 'red', attrs=['bold'])} ")
        originalUserInput = user_input
        user_input = re.sub(r'[^\w\s]', '', user_input).lower()

        if user_input == "exit":
            print(f"{colored('Linus: ', 'green', attrs=['dark', 'bold'])} ", "Bye!")
            break

        response = main_instance.get_response(user_input)
        print(f"{colored('Linus: ', 'green', attrs=['dark', 'bold'])} ", response)