import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def define(word):
    definitions = []
    for syn in wordnet.synsets(word):
        definitions.append(syn.definition())
    return definitions

word = input("word: ")
definitions = define(word)
print("Definitions of", word, ":")
for definition in definitions:
    result = "-", definition
