
toReverse = raw_input("Enter a string:")
 

def reverseString(x):
    beenReversed = ""
    for i in range(len(x), 0, -1):
        beenReversed += x[i-1]
    print beenReversed

reverseString(toReverse)

