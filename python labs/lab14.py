#lottery pick 6
import random
def pick6():
    num_list = []
    n = 0
    while n < 6:
        num = random.randint(1,99)
        num_list.append(num)
        n += 1
    return num_list
def num_matches(winning, ticket):
    matches = []
    for pos, value in enumerate(winning):
        if value == ticket[pos]:
            matches.append(ticket[pos])
            return len(matches)
        else:
            return 0
winnings_dict= {0: 0, 1: 4, 2 : 7, 3: 100, 4 : 50000, 5 : 1000000, 6 : 25000000}
cost = 0
winnings = 0
for game in range(0,100000):
    x = pick6()
    #print(x)
    y = pick6()
    #print(y)
    cost -= 2
    winnings += winnings_dict[num_matches(x, y)]
    #if num_matches(x,y) != 0:
        #print(x,y)
    #print(num_matches(x,y))
    #print(winnings)
bal = cost + winnings
roi = ((winnings - abs(cost))/abs(cost))
print(f'winnings: {winnings}')
print(f'balance: {bal}')
print(f'ROI: {roi}')