#guess_the_number2.py
import random

num1 = random.randint(1,10)
user_guess = input(f'What number am I thinking of between 1 and 10?:')
user_guess = int(user_guess)
guess_num = 0
while True:
    if user_guess == num1:
        print('correct!')
        guess_num = guess_num + 1
        print(f'It only took you {guess_num} tries!')
        break

    elif user_guess != num1:
        print('try again')
        user_guess = input(f'What number am I thinking of between 1 and 10?:')
        user_guess = int(user_guess)
        guess_num = guess_num +1