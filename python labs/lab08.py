#make_change
user_money=float(input(f'Enter how much money you have in dollars and cents:'))
user_amount = int(user_money* 100)
user_quarters = 0
user_dimes = 0
user_nickles = 0
user_pennies = 0
user_change = 0
while True:
    if user_amount // 25 > 0:
        user_quarters = user_amount // 25
        user_amount -=  user_quarters * 25

    if user_amount // 10 > 0:
        user_dimes = user_amount // 10
        user_amount -= user_dimes *10

    if user_amount // 5 > 0:
        user_nickles = user_amount // 5
        user_amount -= user_nickles * 5

    if user_amount // 1 > 0:
        user_pennies = user_amount //1
        user_amount -= user_pennies

    elif user_amount == 0:
        print(f' You can have {user_quarters} quarters,{user_dimes} dimes, {user_nickles} nickles and {user_pennies} pennies')
        break