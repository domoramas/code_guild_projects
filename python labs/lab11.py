#simple calculator
while True:
    operation = input("What operation would you like to perform:")
    while operation not in ['+','-', '*', '/', "done"]:
        print("invalid")
        operation = input("What operation would you like to perform:")
    if operation == "done":
        break    
    num1 = float(input("What is the first number?:"))
    num2 = float(input("What is the second number?:")) 
    if operation == "+":
        print (num1 + num2)
    elif operation == "-":
        print (num1 - num2)
    elif operation == "*":
        print (num1 - num2)
    elif operation == "/":
        print (num1 / num2)
