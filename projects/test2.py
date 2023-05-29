import random_word

# Generate a random word
def go():
    word_generator = random_word.RandomWords()
    random_words = word_generator.get_random_word()
    print(random_words)
    input('')
    go()

input('')
go()