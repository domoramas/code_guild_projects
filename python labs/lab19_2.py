#black jack advice 
def blackjack_adv(x,y,z):
    card_dict = {
    "A" : 1, "2": 2, "3" : 3, "4": 4,
    "5": 5, "6" : 6, "7": 7, "8": 8, 
    "9" : 9, "10" : 10, "J": 10, "Q": 10, "K": 10
    }
    total = (card_dict[x] + card_dict[y] + card_dict[z])
    if total < 12 and  "A" in (x,y,z):
        total = total + 10
    if total < 17:
        print(f"{total} Hit")
    elif total >= 17 and total <21:
        print(f"{total} Stay")
    elif total == 21:
        print(f"{total} Blackjack!")
    elif total > 21:
        print(f"{total} Already Busted")


first_card = input("What's your first card?: ").upper()
second_card = input("What's your second card?: ").upper()
third_card = input("What's your third card?: ").upper()
blackjack_adv(first_card,second_card,third_card)
        