#lists 1
def random_element(a):
        import random
        i = random.randint(0,len(a))
        return a[i]
fruits = ['apples', 'bananas', 'pears']
#print(random_element(fruits))

#lists 2
def REPL():
        num_list = []
        while True:
                num = input("Enter a number (or 'done'):")
                if num != "done":
                        num_list.append(num)
                elif num == "done":
                        print(num_list)
                        break

#REPL()

#lists 3
def eveneven(x):
        evens = []
        for num in x:
                if num %2 == 0:
                        evens.append(num)
        if len(evens) %2 == 0:
                return True
        else:
                return False
#print(eveneven([5, 6, 2]))
#print(eveneven([5, 5, 2]))

#lists 4
def print_every_other(x):
        #n = 0
        #while n < (len(x)):
                #print(x[n], end=" ") 
                #n += 2
        #print()

        for n in range(0,len(x),2):
                print(n, end=" ")
        print()        

#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#print_every_other(nums)

#lists 5
def reverse(nums):
        nums.reverse()
        return nums
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#print(reverse(nums))

#lists 6
def extract_less_than_ten(nums):
        less_than_10 = []
        for n in nums:
                if n < 10:
                        less_than_10.append(n)
        return less_than_10

#cats = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
#print(extract_less_than_ten(cats))

#lists 7 
def common_elements(nums1, nums2):
        common = []
        for n in nums1:
                if n in nums2 and n not in common:
                        common.append(n)
        return common
#cats = [5,6,8,10,3,2,5,7]
# dogs = [1,2,3,4,5]
# print(common_elements(cats,dogs))

#list #8
def combine(nums1,nums2):
        combined = []
        for i in range(len(nums1)):
                combined.append(nums1[i])
                combined.append(nums2[i])
        return combined
#print(combine(['a','b','c'],[1,2,3]))

#list 9
def find_pair(nums, target):
        t = target
        pairs=[]
        for num in nums:
                if num < t:
                        y = t - num
                        if y in nums and (y, num) not in pairs:
                                        pairs.append((num, y))
        return pairs

# list 10
def merge(list1, list2):
        merged = []
        for i in range(len(list1)):
                merged.append((list1[i], list2[i]))
        return merged

# print(merge([5,2,1], [6,8,2]))

#list 11
def combine_all(listoflist):
        combined= []
        for i in range(len(listoflist)):
                for num in range(len(listoflist[i])):
                        combined.append(listoflist[i][num])
        return combined
#nums = [[5,2,3],[4,5,1],[7,6,3]]
# print(combine_all(nums))

#list 12
def fibonacci(n):
        f_list= []
        for num in range(n):
                # print(num)
                if num == 1 or num == 0:
                        f_list.append(1)
                else:       
                        f_list.append((f_list[num-1])+(f_list[num-2]))
        return f_list    
#print(fibonacci(18))

#list 13
def minimum(nums):
        nums.sort()
        return nums[0]
        
def maximum(nums):
        nums.sort()
        return nums[-1]
def mean(nums):
        total = 0
        for num in nums:
                total += num
        return total/len(nums)
# def mode(nums):
       

#list 14
def find_unique(nums):
        unique_nums = []
        for num in nums:
                if num not in unique_nums:
                        unique_nums.append(num)   
        return unique_nums               
      
# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155, 155]
# print(find_unique(nums))