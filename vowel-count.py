
toBeCounted = "Hello world I am a chicken"
numVowels = 0
for letter in toBeCounted:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numVowels += 1
    

print "You have "  + str(numVowels) + " vowels, CHICKEN!!!"