#Takes user input and returns pig latin

strInput = input('Give us your best English word or phrase: ')
wordList = strInput.split(' ')

def pigTranslate(phrase):
    outputString = ''
    pigLatin = "ay"
    for word in phrase:
        outputString += word[1:] + word[0].lower() + pigLatin + ' '
    return outputString

print(pigTranslate(wordList))
