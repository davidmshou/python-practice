#
#Translates user input into Pig Latin
#

import string

#user input to list of strings
wordList = raw_input("Give me a phrase!: ").split()

vowels = ['a', 'e', 'i', 'o', 'u']
endPoints = ['?', '.', '!',',',':',';']
#add features:depigifier, startup wizard or handle args/modifiers

#helper function to convert a given word
def wordToPig(word):
    #lowercase each word as they come in
    word = word.lower()
    newWord = ''
    aySuffix = "ay"
    waySuffix = 'way'
    firstLetter = word[0]
    noFirstLetter = word[1: ]
    lastChar = ''

    #rearrange punctuation
    for i in range(0,len(word)):
        if word[i] in endPoints:
            lastChar = word[i]
            word = word[0:i] + word[i + 1: ]
            
    #if starts with diphthong then move whole diphthong
    if word[0:2] == 'ch' or word[0:2] == 'qu' or word[0:2] == 'th' \
            or word[0:2] == 'ph':
        firstLetter = word[0:2]
        noFirstLetter = word[2: ]
        newWord += noFirstLetter + firstLetter + aySuffix + lastChar
    #if starts with vowel just end with way
    elif word[0] in vowels:
        newWord += firstLetter + noFirstLetter + waySuffix + lastChar
    #if only 1 char long do nothing
    elif len(word) < 2:
        newWord += firstLetter + lastChar
    else:
        firstLetter = word[0]
        noFirstLetter = word[1: ]
        newWord += noFirstLetter + firstLetter + aySuffix + lastChar

    return newWord

#helper function to convert words back to english
def wordFromPig(word):
    word = word.lower()
    newWord = ''
    aySuffix = "ay"
    waySuffix = 'way'
    firstLetter = word[0]
    noFirstLetter = word[1: ]
    lastChar = ''

#translates to pig latin given a list of strings
def pigTranslate(phrase):
    newPhrase = ""
    for word in phrase:
        newPhrase += wordToPig(word) + ' '
        
    #capitalize the first letter
    capFirst = newPhrase[0]
    newPhrase = capFirst.upper() + newPhrase[1: ]
    
    #return our piggy phrase minus the space at the very end
    return newPhrase[0:len(newPhrase) - 1]

     
#print(pigTranslate(wordList))
#print('')
#print('ankthay ouyay, oodbyegay')

#translate pig latin back to english
def depigify(phrase):
    newPhrase = ''
    for word in phrase:
        newPhrase += wordFromPig(word) + ' '

    #capitalize the first letter
    capFirst = newPhrase[0]
    newPhrase = capFirst.upper() + newPhrase[1: ]
    
    #return our english phrase minus the space at the very end
    return newPhrase[0:len(newPhrase) - 1]

print(depigify(wordList))
print('')
print('GOODBYE')
