#magic 8 ball
import random

answers = ('It is certain','It is decidedly so', 'Without a doubt', 'Yes, definitely', 'Most likely', 'Ask again later', "As I see it, yes", 'Maybe so', 'Don\'t count on it')

print("Welcome to the Magic 8 Ball")
while True:
    question = input("Type in your question or 'done' if finished:")
    if question == "done":
        break
    elif question:    
        print(random.choice(answers))
    else:
        print("you didn't type anything")

