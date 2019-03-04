#number to phrase

def number_phrase(x):
    hundreds_digit = x // 100
    tens_digit = x % 100 // 10
    ones_digit = x % 10
    number_dict = {
        1: ['one','ten','one-hundred'], 2: ['two',"twenty","two-hundred"], 3 : ['three',"thirty","three-hundred"], 
        4: ['four',"forty","four-hundred"], 5: ['five',"fifty",'five-hundred'], 6: ["six", "sixty", "six-hundred"],
        7: ["seven","seventy","seven_hundred"], 8: ["eight","eighty", "eight-hundred"], 9: ['nine',"ninety","nine-hundred"],0 : ['', '', '']
        }
    teens_dict= {
        1 : "eleven", 2 : 'twelve', 3 : "thirteen", 4 : "fourteen", 
        5 : "fifteen", 6 : "sixteen", 7 : "seventeen", 8 : "eighteen", 9: "nineteen"
        }
    if hundreds_digit < 1:
        if tens_digit <1 and ones_digit >0:
            print(number_dict[ones_digit][0])
            if ones_digit == 0:
                print("zero")
        elif tens_digit == 1 and ones_digit >0:
            print(teens_dict[ones_digit])
        elif tens_digit >0:
            print(f'{number_dict[tens_digit][1]}-{number_dict[ones_digit][0]}')
    elif hundreds_digit >0: 
        if tens_digit <1 and ones_digit >= 0:
            print(f'{number_dict[hundreds_digit][2]} {number_dict[ones_digit][0]}')
        if tens_digit == 1 and ones_digit >0:
            print(f'{number_dict[hundreds_digit][2]} {teens_dict[ones_digit]}')
        elif tens_digit >0:
            print(f'{number_dict[hundreds_digit][2]} {number_dict[tens_digit][1]}-{number_dict[ones_digit][0]}')

    
num = int(input("give me a number to translate:"))
number_phrase(num)
        

    