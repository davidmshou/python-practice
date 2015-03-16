
"""userInput = raw_input("Give me a phrase!: ")
wordList = userInput.split()

def pigTranslate(phrase):
    outputString = ""
    for i in phrase:
        if i[0:1].lower() == "ch" or i[0:1].lower() == "qu":
            firstLetter = i[0:1]
            noFirstLetter = i[2: ]
        else:
            firstLetter = i[0].lower()
            noFirstLetter = i[1: ]
        return firstLetter
        return noFirstLetter
        pigLatin = "ay"
        outputString += noFirstLetter + firstLetter + pigLatin + " "
    return outputString

print pigTranslate(wordList)"""

#userInput = raw_input("Give me a phrase!: ")
#wordList = userInput.split()
wordList = 'Cheer up laddo its only a quiescent quandary'.split()

def pigTranslate(phrase):
    outputString = ""
    for i in phrase:
        if i[0:2].lower() == "ch" or i[0:2].lower() == "qu":
            firstLetter = i[0:2]
            noFirstLetter = i[2: ]
        else:
            firstLetter = i[0].lower()
            noFirstLetter = i[1: ]
        pigLatin = "ay"
        outputString += noFirstLetter + firstLetter + pigLatin + " "
    return outputString

print pigTranslate(wordList)




