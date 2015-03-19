import string



def stripPunctuation(phrase):
    newPhrase = ''.join(ch for ch in phrase if ch not in \
                        string.punctuation)
    return newPhrase

userInput = input('give me a phrase: ')
print(stripPunctuation(userInput))
