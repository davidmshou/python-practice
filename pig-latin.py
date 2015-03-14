
"""toTranslate = "Hello"

firstLetter = toTranslate[0].lower()

noFirstLetter = toTranslate[1: ]

pigLatin = "ay"

print noFirstLetter + "-" + firstLetter + pigLatin """

def pigTranslate(word):
    firstLetter = word[0].lower()
    noFirstLetter = word[1: ]
    pigLatin = "ay"
    print noFirstLetter + "-" + firstLetter + pigLatin

pigTranslate("Hello")
