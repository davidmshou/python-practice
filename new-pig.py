
userInput = raw_input("Give me a phrase!: ")
wordList = userInput.split()

def pigTranslate(phrase):
    outputString = ""
    for i in phrase:
        firstLetter = i[0].lower()
        noFirstLetter = i[1: ]
        pigLatin = "ay"
        outputString += noFirstLetter + firstLetter + pigLatin + " "
    return outputString

print pigTranslate(wordList)




