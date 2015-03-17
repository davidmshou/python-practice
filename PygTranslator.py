#Pyg Translator v0.2
#by Russell Graham

import sys
import string

print('###Pyg Translator v0.2###')


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

def pigFromEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('bye')
    sys.exit()

def pigToEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('bye')
    sys.exit()


def goatFromEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('bye')
    sys.exit()


def goatToEnglish(phrase):
    print('''this function isn't finished yet!''')
    input('bye')
    sys.exit()

    
if userInput == 'A'.lower():
    userInput = input('Give me a phrase: ')
    print(pigFromEnglish(userInput))
elif userInput == 'B'.lower():
    userInput = input('Give me a phrase: ')
    print(pigToEnglish(userInput))
elif userInput == 'C'.lower():
    userInput = input('Give me a phrase: ')
    print(goatFromEnglish(userInput))
elif userInput == 'D'.lower():
    userInput = input('Give me a phrase: ')
    print(goatToEnglish(userInput))
elif userInput == 'P'.lower():
    userInput = input('Give me a phrase: ')
    userInput = userInput.translate(string.maketrans("",""), \
                                    string.punctuation)
    print(userInput)
    print()
    input('bye')
    sys.exit()
elif userInput == 'L'.lower():
    userInput = input('Give me a phrase: ')
    userInput = userInput.lower()
    print()
    input('bye')
    sys.exit()
elif userInput == 'U'.lower():
    userInput = input('Give me a phrase: ')
    userInput = userInput.upper()
    print()
    input('bye')
    sys.exit()
elif userInput == 'UP'.lower() or userInput == 'PU'.lower():
    userInput = input('Give me a phrase: ')
    userInput = userInput.translate(string.maketrans("",""), \
                                    string.punctuation)
    userInput = userInput.upper()
    print()
    input('bye')
    sys.exit()
elif userInput == 'UL'.lower() or userInput == 'LU'.lower():
    userInput = input('Give me a phrase: ')
    userInput = userInput.translate(string.maketrans("",""), \
                                    string.punctuation)
    userInput = userInput.lower()
    print()
    input('bye')
    sys.exit()




