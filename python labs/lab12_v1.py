#guess_the_number.py
import random
#user can guess ten times
num1 = random.randint(1,10)
user_guess = input(f'What number am I thinking of between 1 and 10?:')
user_guess = int(user_guess)
guess_num = 0
while guess_num < 11:
    if user_guess == num1:
        print('correct!')
        break
    elif user_guess != num1:
        print('try again')
        user_guess = input(f'What number am I thinking of between 1 and 10?:')
        user_guess = int(user_guess)
        guess_num = guess_num +1
if guess_num == 10:
    print("out of tries, you've lost")
