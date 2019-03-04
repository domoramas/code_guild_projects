# comperhensions practice
import string
#1
def comp_power2(n):
       return [2**x for x in range(n)] 
#print(comp_power2(10))

#2
def comp_evens(n):
        return [x for x in range((n+1)*2) if x >0 and x % 2 == 0]
#print(comp_evens(10))

#3
def comp_swap(n):
        return {v:k for k,v in n.items()}

#print(comp_swap({'a': 1, 'b': 2}))

#4
def ascii_alpha():
        return {chr(i):i for i in range((ord("a")),(ord("z")+1))}

#print(ascii_alpha())