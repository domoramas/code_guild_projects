#number to phrase

def number_roman(x):
    hundreds_digit = x // 100
    tens_digit = x % 100 // 10
    ones_digit = x % 10
    number_dict = {
        1: ['I','X','C'], 2: ['II',"XX","CC"], 3 : ['III',"XXX","CCC"], 
        4: ['IX',"XL","CD"], 5: ['V',"L",'D'], 6: ["VI", "LX", "DC"],
        7: ["VII","LXX","DCC"], 8: ["XIII","LXXX", "DCCC"], 9: ['IX',"XC","CM"],0 : ['', '', '']
        }
    if hundreds_digit < 1:
        if tens_digit <1 and ones_digit >0:
            print(number_dict[ones_digit][0])
        elif tens_digit >0:
            print(f'{number_dict[tens_digit][1]}{number_dict[ones_digit][0]}')
    elif hundreds_digit >0: 
        if tens_digit <1 and ones_digit >= 0:
            print(f'{number_dict[hundreds_digit][2]}{number_dict[ones_digit][0]}')
        elif tens_digit >0:
            print(f'{number_dict[hundreds_digit][2]}{number_dict[tens_digit][1]}{number_dict[ones_digit][0]}')


    
num = int(input("give me a number to translate:"))
number_roman(num)
        

    