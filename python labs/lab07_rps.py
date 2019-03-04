#rock_paper_scissors_adv.py
import random
rps_dict = {
    'rock': ['paper', 'scissors'], 
    'paper' : ['scissors', 'rock'], 
    'scissors' : ['rock','paper' ]}
    
print('Lets play Rock, Paper, Scissors!!!')
user_win = 0
cp_win = 0
while True:
    chosen_move = input('Make your move! rock, paper or scissors?:').lower()
    while chosen_move not in rps_dict.keys():
        chosen_move = input('Make your move! rock, paper or scissors?:')
    cp_move = random.choice(list(rps_dict.keys()))
    if rps_dict[chosen_move][0] == cp_move:
        print(f'Computer choses: {cp_move}\n...you lose.')
        cp_win += 1
    elif rps_dict[chosen_move][1] == cp_move:
        print(f'Computer choses: {cp_move}\n...you win!')
        user_win += 1
    elif chosen_move == cp_move:
        print(f"Computer choses: {cp_move}\n...it's a tie!")
    exit_string = input('Do you want to play again? y/n :')
    if exit_string == "n":
        print(f'Scoreboard: You - {user_win} || Computer - {cp_win}')
        break