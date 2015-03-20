
piggy = "Ellohay orldway".split()

def dePigify(phrase):
    output = ""
    for i in phrase:
        firstLetter = i[len(i) - 3]
        noFirstLetter = i[0:len(i) - 3]
        output += firstLetter + noFirstLetter + " "
    return output.lower()

print dePigify(piggy)
