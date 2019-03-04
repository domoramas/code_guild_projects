#average with user input


print("Lets find an average!") #title
nums = [] #list to fill
while True:
    n = input("Enter a number or 'done': ")
    if  n == 'done':
        break
    elif n != 'done':
        if n not in ['0','1','2','3','4','5','6','7','8','9',] :
            print("Not a number!")
            n = input("Enter a number or 'done': ")
        else:
            nums.append(int(n))   
total = 0
for num in nums:
    total += num
#print(nums)
#print(total)
print(f"Average: {(total/len(nums))}")
