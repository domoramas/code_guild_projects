#average

nums = [5, 0, 8, 3, 4, 1, 6]
    
def average(x):
    total = 0
    for num in nums:
        total += num
    print(total/(len(nums)))

average(nums)

    