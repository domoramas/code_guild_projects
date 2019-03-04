#problem1
def is_even(a):
    if a % 2  == 0:
       return True
    else:
        return False
#print(is_even(6))

#problem2
def opposite(a,b):
    if a < 0 and b >= 0:
       return True
    if a >= 0 and b < 0:
       return True
    else:
       return False
#print(opposite(10, -1))
#print(opposite(2,3))
#print(opposite(-1,-1))
#print(opposite(-10, 9))

#problem 3
def near_100(num):
    if abs(num - 100) <=10:
        return True
    else:
        return False
#print(near_100(50))
#print(near_100(99))
#print(near_100(105))

#problem 4
def maximum_of_three(a,b,c):
    return max(a,b,c)
#print(maximum_of_three(5,6,2))
#print(maximum_of_three(-4,3,10))

#problem 5
def power():
    for x in range(0,21):
        print(2**x)
#power()
