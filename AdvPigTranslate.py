#Translates user input into Pig Latin

#user input to list of strings
wordList = 'this is a phrase dont be sad instead be rad'.split()#raw_input("Give me a phrase!: ").split()
vowels = ['a', 'e', 'i', 'o', 'u']
#add features: handle punctuation, depigify words and phrases, setup wizard or handle user args

#helper function to convert a given word
def wordToPig(word):
    word = word.lower()
    newWord = ''
    pigSuffix = "ay"
    firstLetter = word[0:1]
    noFirstLetter = word[1: ]
    #if word starts with vowel or a diphthong
    if word[0:2] == 'ch' or word[0:2] == 'qu' or word[0:2] == 'th' or word[0:2] == 'ph' or word[0] in vowels and len(word) > 1:
        firstLetter = word[0:2]
        noFirstLetter = word[2: ]
        newWord += noFirstLetter + firstLetter + pigSuffix
    #if word is only 2 chars long and starts with vowel
    elif len(word) == 2 and word[0] in vowels:
        newWord += firstLetter + noFirstLetter + pigSuffix
    elif len(word) == 2:
        newWord += noFirstLetter + firstLetter + pigSuffix
    #if word is only 1 char do nothing to it
    elif len(word) < 2:
        newWord += firstLetter + noFirstLetter
    #if no special case then do standard translation
    else:
        firstLetter = word[0]
        noFirstLetter = word[1: ]
        newWord += noFirstLetter + firstLetter + pigSuffix

    return newWord

#translates to pig latin given a list of strings
def pigTranslate(phrase):
    newPhrase = ""
    for word in phrase:
        newPhrase += wordToPig(word) + ' '
    #return our piggy phrase minus the space at the very end
    return newPhrase[0:len(newPhrase) - 1]
         
print(pigTranslate(wordList))
print('')
print('ankthay ouyay, oodbyegay')