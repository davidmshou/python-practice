#Translates user input into Pig Latin

#user input to list of strings
wordList = raw_input("Give me a phrase!: ").split()

#add features: handle diphthongs, phrases, punctuation,
#depigify words and phrases, setup wizard or handle user args

#helper function to convert a given word
def wordToPig(word):
    word = word.lower()
    newWord = ''
    pigLatin = "ay"
    firstLetter = word[0]
    noFirstLetter = word[1: ]

    newWord += noFirstLetter + firstLetter + pigLatin
    return newWord

print(wordToPig('this'))


#translates given a list of strings

def pigTranslate(phrase):
    newPhrase = ""
    for word in phrase:
        newPhrase += wordToPig(word) + ' '
    #return our piggy phrase minus the space at the very end
    return newPhrase[0:len(newPhrase) - 1]
         
print pigTranslate(wordList)
print('')
print('Goodbye')
