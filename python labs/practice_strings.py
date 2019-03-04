#string 1
def double_word():
    word = input("Give me a word:")
    new_string = []
    for l in word:
        new_string.append(l*2)
    return("".join(new_string))
#print(double_word())

#string #2
def missing_char(word):
    option =[]
    for char in word:
        option.append(''.join(word.split(char,1)))
    return option
#print(missing_char("kitten"))

#string #3
import string
def latest_letter(word):
        word = list(word)
        word.sort()
        return word[-1]
#print(latest_letter(aslkfjlwpmpwrz))

#string #4
def count_hi(x):
        return (x.count('hi'))
#print(count_hi("hihihi"))

#string #5
def cat_dog(x):
        if x.count('dog') == x.count('cat'):
                return True
        else:
                return False
#print(cat_dog('catdog'))
#print(cat_dog('catcat'))
#print(cat_dog('catdogcatdog'))

#string #6
def count_letter(letter, word):
        return word.count(letter)
#print(count_letter('i', 'antidisestablishmentterianism'))
#print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))

#string #7
def lower_case(word):
        word =word.strip()
        word = word.lower()
        return word

#print(lower_case("SUPER!"))
#print(lower_case("        NANNANANANA BATMAN        "))