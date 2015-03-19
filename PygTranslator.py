#Pyg Translator v0.2
#by Russell Graham & David Shoubridge

#feature idea:read-aloud feature that returns a phonetic word for
#each letter(c becomes see)

import sys
import string
import re

endPoints = ['?', '.', '!',',',':',';']
vowels = ['a','e','i','o','u']
#totally made a script in Python Shell to create this list :D
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', \
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
startText = '###Pyg Translator v0.2###'
helpText = """What do you want to do?
Type:
     A for English-to-Pyg
     B for Pyg-to-English
     C for English-to-Goat
     D for Goat-to-English
     P to strip punctuation
     L for lower case
     U for upper case
     PL or PU for a combination
     H for Help Text"""

    
def englishToPig(phrase):
    newPhrase = ''
    print('This feature is a work-in-progress.')
    for word in phrase:
        newPhrase += etopHelper(word) + ' '
    print('\n' + newPhrase[0].upper() + newPhrase[1:len(newPhrase) - 1] \
          + '\n\nDone\n')


def etopHelper(word):
    word = word.lower()
    newWord = ''
    consSuffix = "ay"
    vowelSuffix = 'way'
    firstLetter = word[0:1]
    noFirstLetter = word[1: ]
    lastChar = ''
    #make some attempt to rearrange punctuation
    for i in range(0,len(word)):
        if word[i] in endPoints:
            lastChar = word[i]
            word = word[0:i] + word[i + 1: ]
    
    #if word starts with a diphthong
    if word[0:2] == 'ch' or word[0:2] == 'qu' or word[0:2] == 'th' or \
           word[0:2] == 'ph':
        firstLetter = word[0:2]
        noFirstLetter = word[2: ]
        newWord += noFirstLetter + firstLetter + consSuffix + lastChar
    #if word starts with vowel
    elif word[0] in vowels:
        newWord += firstLetter + noFirstLetter + vowelSuffix + lastChar
    #if no special case then do standard translation
    else:
        firstLetter = word[0]
        noFirstLetter = word[1: ]
        newWord += noFirstLetter + firstLetter + consSuffix + lastChar

    return newWord


def pigToEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('Goodbye')
    sys.exit()


def englishToGoat(phrase):
    print('''this function isn't finished yet!''')
    input('Goodbye')
    sys.exit()


def goatToEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('Goodbye')
    sys.exit()


def stripPunctuation(phrase):
    newPhrase = ''.join(ch for ch in phrase if ch not in \
                        string.punctuation)
    return newPhrase


#program start
print(startText + '\n' + helpText)
while 1:
    userInput = input()
    
    if userInput.lower() == 'a':
        userInput = input('Give me a phrase: ').split()
        print(englishToPig(userInput))
    elif userInput.lower() == 'b':
        userInput = input('Give me a phrase: ').split()
        print(pigToEnglish(userInput))
    elif userInput.lower() == 'c':
        userInput = input('Give me a phrase: ').split()
        print(englishToGoat(userInput))
    elif userInput.lower() == 'd':
        userInput = input('Give me a phrase: ').split()
        print(goatToEnglish(userInput))
    elif userInput.lower() == 'p':
        newPhrase = input('Give me a phrase: ')
        print(stripPunctuation(newPhrase))
        print()
        input('Goodbye')
    elif userInput.lower() == 'l':
        newPhrase = input('Give me a phrase: ')
        print(newPhrase.lower())
        print()
        input('Goodbye')
    elif userInput.lower() == 'u':
        newPhrase = input('Give me a phrase: ')
        print(newPhrase.upper())
        print()
        input('Goodbye')
    elif userInput.lower() == 'up' or userInput.lower() == 'pu':
        newPhrase = input('Give me a phrase: ')    
        print(stripPunctuation(newPhrase).upper())
        print()
        input('Goodbye')
    elif userInput.lower() == 'pl' or userInput.lower() == 'lp':
        newPhrase = input('Give me a phrase: ')
        print(stripPunctuation(newPhrase).lower())
        print()
        input('Goodbye')
    elif userInput.lower() == 'h':
        print(helpText)

