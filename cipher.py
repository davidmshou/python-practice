"""import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)

print(alphabet_list)

message_text = "what is a baggins"

cipher_list = list(alphabet_list)
random.shuffle(cipher_list)

print(cipher_list)

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text"""

import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)

print(alphabet_list)

message_text = "gvxpuogvxogvxoyapt"

cipher_list = ['z', 'k', 'q', 'p', 's', ' ', 'd', 'g', 'a', 'e', 'y', 'h', 'f', 'n', 'v', 'm', 'b', 'l', 't', 'r', 'c', 'i', 'x', 'w', 'u', 'j', 'o']

#random.shuffle(cipher_list)

cipher_text = ""

for x in message_text:
    index = cipher_list.index(x)
    cipher_char = alphabet_list[index]
    cipher_text += cipher_char

print cipher_text
