#Pyg Translator v0.2
#by Russell Graham

import sys
import string

print('###Pyg Translator v0.2###')
print()
print('''What do you want to do? \n
Type: /n
A for English-to-Pyg /n
B for Pyg-to-English /n
C for English-to-Goat/n
D for Goat-to-English/n
P to strip punctuation/n
L for lower case/n
U for upper case/n
PL or PU for a combination/n''')
userInput = input()

#newPhrase = ''

vowels = ['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', \
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def englishToPig(phrase):
    newPhrase = ''
    print('''this function isn't finished yet!''')
    for word in phrase:
        newPhrase += etopWord(word) + ' '
        print(newPhrase)#[0:len(newPhrase) - 1])
    
    input('Goodbye')
    sys.exit()

def etopWord(word):
    #for i in range(0,len(word))
    word = word.lower()
    newWord = ''
    consSuffix = "ay"
    vowelSuffix = 'way'
    firstLetter = word[0:1]
    noFirstLetter = word[1: ]
    #if word starts with a diphthong
    if word[0:2] == 'ch' or word[0:2] == 'qu' or word[0:2] == 'th' or \
           word[0:2] == 'ph':
        firstLetter = word[0:2]
        noFirstLetter = word[2: ]
        newWord += noFirstLetter + firstLetter + consSuffix
    #if word starts with vowel
    elif word[0] in vowels:
        newWord += firstLetter + noFirstLetter + vowelSuffix
    #if no special case then do standard translation
    else:
        firstLetter = word[0]
        noFirstLetter = word[1: ]
        newWord += noFirstLetter + firstLetter + consSuffix

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

    
if userInput.lower() == 'a':
    userInput = input('Give me a phrase: ')
    print(englishToPig(userInput))
elif userInput.lower() == 'b':
    userInput = input('Give me a phrase: ')
    print(pigToEnglish(userInput))
elif userInput.lower() == 'c':
    userInput = input('Give me a phrase: ')
    print(englishToGoat(userInput))
elif userInput.lower() == 'd':
    userInput = input('Give me a phrase: ')
    print(goatToEnglish(userInput))
elif userInput.lower() == 'p':
    newPhrase = input('Give me a phrase: ')
    print(stripPunctuation(newPhrase))
    print()
    input('Goodbye')
    sys.exit()
elif userInput.lower() == 'l':
    newPhrase = input('Give me a phrase: ')
    print(newPhrase.lower())
    print()
    input('Goodbye')
    sys.exit()
elif userInput.lower() == 'u':
    newPhrase = input('Give me a phrase: ')
    print(newPhrase.upper())
    print()
    input('Goodbye')
    sys.exit()
elif userInput.lower() == 'up' or userInput.lower() == 'pu':
    newPhrase = input('Give me a phrase: ')    
    print(stripPunctuation(newPhrase).upper())
    print()
    input('Goodbye')
    sys.exit()
elif userInput.lower() == 'pl' or userInput.lower() == 'lp':
    newPhrase = input('Give me a phrase: ')
    print(stripPunctuation(newPhrase).lower())
    print()
    input('Goodbye')
    sys.exit()
