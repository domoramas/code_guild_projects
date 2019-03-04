#hangman game
import random

def load_words(path):
    with open(path) as master_words:
        word_list = master_words.read().strip('\n').split('\n')

    hangman_words = []
    for words in word_list:
        if len(words) > 5:
            hangman_words.append(words)

    return hangman_words

hangman_words = load_words("/Users/damianoramas/Desktop/redmage/class_redmage/1 Python/data/english.txt")


HANGMANPICS = ['''

  

       +---+
           |
           |
           |
           |
           |
           |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''','''

    

       +---+
       |   |
       |   |
           |
           |
           |
           |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''

 

       +---+
       |   |
       |   |
       |   |
       O   |
           |
           |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''

    

       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
           |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''

 

       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
       |   |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''

 

       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
      /|   |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''



       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
      /|\  |
           |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''', '''

 

       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
      /|\  |
       |   |
           |
     ¯¯¯¯¯¯|
           |
           |
     =========''','''

    

       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
      /|\  |
       |   |
      /    |
     ¯¯¯¯¯¯|
           |
           |
     =========''','''



       +---+
       |   |
       |   |
       |   |
       O   |
       |   |
      /|\  |
       |   |
      / \  |
     ¯¯¯¯¯¯|
           |
           |
     =========''','''

 

       +---+
       |   |
       |   |
       |   |
       X   |
       |   |
      /|\  |
       |   |
      / \  |
           |
           |
           |
     =========''']

word_answer = random.choice(hangman_words)
guess_list = []
num_guess = 10

loop_flag = True
while loop_flag:
      
      win_lose_flag = True # For winning and loosing
      
      guess_string = ''
      for l in word_answer:
            if l in guess_list:
                  guess_string += l + " "
            else:
                  guess_string += "_ "

      if guess_string.split() == list(word_answer):
            print("\nYou win!\n")
            print(guess_string.replace(" ","").upper())
            win_lose_flag = False
      

      if num_guess == 0:
            print(f'\nYou lose....the answer was {word_answer}\n')
            win_lose_flag = False
      
      print(HANGMANPICS[10-num_guess])

      print(word_answer) # just for testing
      
      print (guess_string)
      print(f'You have {num_guess} guesses remaining')
      
      if win_lose_flag == True:
            user_guess = ''
            while len(user_guess) != 1:
                  user_guess = input("Guess a letter: ")

            if user_guess not in guess_list:
                  guess_list.append(user_guess)
                  if user_guess not in word_answer:
                        num_guess -= 1
            else:
                  guess_print = ", ".join(guess_list)
                  print(f"you already guessed {guess_print} ")

      if win_lose_flag == False:
            end_input = ''
            while end_input != 'y' and end_input != 'n':
                  end_input = input('Would you like to play again? (y/n) > ').lower()
            
            if end_input == 'y':
                  word_answer = random.choice(hangman_words)
                  guess_list = []
                  num_guess = 10
            else:
                  loop_flag = False


