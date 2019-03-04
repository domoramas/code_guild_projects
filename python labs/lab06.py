#password_gen_adv.py
import string
import random
password_gen = ''
#n = input("How many characters do you want your password to be?:")
print("Lets make a password!")
count = int(input("How many characters long do you want it to be: "))
l = int(input("How many uppercase letters?:"))
p = int(input('How many symbols?:'))
num = int(input('How many numbers?:'))
for char in range(0, (l)):
        password_gen = password_gen + random.choice(string.ascii_uppercase)
for char in range(0, (p)):
        password_gen = password_gen + random.choice(string.punctuation)
for char in range(0, (num)):
        password_gen = password_gen + random.choice(string.octdigits)
for char in range(0, (count - (l+p+num))):
        password_gen = password_gen + random.choice(string.ascii_lowercase)
password_gen = list(password_gen)
random.shuffle(password_gen)

print("".join(password_gen))
