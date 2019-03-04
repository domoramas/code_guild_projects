#Palindrom and anagram checker

def check_palindrome(word):
    if list(word) == list(reversed(word)):
        return True
    else:
       return False
def palindrome_checker():
    word = input("enter a word: ")
    if (check_palindrome(word)) == True:
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is not a palindrome')

#palindrome_checker()

def check_anagram(x,y):
    x = x.lower()
    x = x.replace(" ", "")
    x = list(x)
    x.sort()
    y = y.lower()
    y = y.replace(" ", "")
    y = list(y)
    y.sort()
    if x == y:
        return True
    else:
        return False
def anagram_checker():
    first_word = input('enter the first word: ')
    second_word = input("enter the second word: ")
    if (check_anagram(first_word, second_word)) == True:
        print (f'{first_word} and {second_word} are anagrams')
    else:
        print (f'{first_word} and {second_word} are not anagrams')

#anagram_checker()
while True:
    p_or_a = input("Would you like to check an anagram or a palindrome or exit?: ")
    if p_or_a == "anagram":
        anagram_checker()
    elif p_or_a == "palindrome":
        palindrome_checker()
    elif p_or_a == "exit":
        break
    else:
        print ("try again")