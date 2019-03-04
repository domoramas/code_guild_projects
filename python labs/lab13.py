#rot_cypher.py
import string

x = int(input("Pick a number between 1 and 26 for your codex: "))
rot_string = string.ascii_lowercase[x:] + string.ascii_lowercase[:x]
decrypt_string = rot_string[-x:] + rot_string[:-x]

def encyrpt(word):
    word_list = list(word.lower())
    new_word = []
    for letter in word_list:
        n = (rot_string[string.ascii_lowercase.index(letter)])
        new_word.append(n)
    return("".join(new_word))

def decrypt(w):
    new_list = list(w)
    old_word = []
    for letter in new_list:
        n = (decrypt_string[rot_string.index(letter)])
        old_word.append(n)
    print("".join(old_word))

word = input("Enter the word you want to encrypt: ")
print(encyrpt(word))
new_word = encyrpt(word)
undo_string = input('Would you like to decrypt the word? Y/N:')
if undo_string.upper() == "Y":
    #word = "".join(new_word)
    word = input("type in encrypted word: ")
    decrypt(word)    
else:
    print("Goodbye!")

