#guess_the_number4.py
import random

num1 = random.randint(1,20)
user_guess = input(f'What number am I thinking of between 1 and 20?:')
user_guess = int(user_guess)
guess_num = 0

while True:
    if user_guess == num1:
        print('correct!')
        guess_num = guess_num + 1
        print(f'It only took you {guess_num} tries!')
        break
    while guess_num < 1:
        print('try again')
        last_guess = user_guess
        print(last_guess)
        user_guess = input(f'What number am I thinking of between 1 and 20?:')
        user_guess = int(user_guess)
        guess_num = guess_num +1   
    if user_guess != num1:
        print(last_guess)
        if abs(num1 - user_guess) < abs(num1 - last_guess):
            print("getting warmer")
        if abs(num1 - user_guess) > abs(num1 - last_guess):
            print("getting colder")
        if abs(num1 - user_guess) == abs(num1 - last_guess):
            print('No closer, try again')
        last_guess = user_guess
        user_guess = input(f'What number am I thinking of between 1 and 20?:')
        user_guess = int(user_guess)
        guess_num = guess_num +1
