import pygame
import random
pygame.init()

words = ['banana', 'cherry', 'chair', 'soccer', 'super', 'computer', 'apple', 
'orange', 'table', 'football', 'keyboard', 'guitar', 'lamp', 'pencil', 'television',
'book', 'garden', 'window', 'globe', 'car', 'dog', 'cat', 'house', 'phone', 'tree', 
'flower', 'pizza', 'cookie', 'bike', 'ocean', 'beach', 'mountain', 'cloud', 'moon', 
'sun', 'star', 'fish', 'bird', 'pen', 'shoes', 'hat', 'shirt', 'pants', 'socks', 
'wallet', 'key', 'door', 'bag', 'smile', 'bottle', 'string', 'parrot', 'mouse']


def sentenceEquals():
    global sentence
    sentenceList = []
    for i in range(25):
        nextWord = random.choice(words)
        sentenceList.append(nextWord)
    sentence = ''
    for i in sentenceList:
        sentence += i + ' '
    print(sentence)
    return sentence
    



def getSentence():
    global sentence
    sentence = sentence

def getNextKey():
    ''