#Takes user input and returns pig latin

strInput = input('Give us your best English word or phrase: ')
wordList = strInput.split(' ')

def pigTranslate(phrase):
    outputString = ''
    pigLatin = "ay"
    for i in range(0,len(phrase)):
        listIndex = phrase[i]
        firstLetter = listIndex[0].lower()
        noFirstLetter = listIndex[1:]
        outputString += noFirstLetter + firstLetter + pigLatin + ' '
    return outputString

print(pigTranslate(wordList))
