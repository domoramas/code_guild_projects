#Peaks and valleys
def peaks(x):
    peaks = {}
    for i in range(1,len(x)-1):
        if (x[i-1]) < x[i] and x[i] > (x[i +1]):
            peaks.update({i : x[i]})  
    return list(peaks.keys())

def valleys(x):
    valleys = {}
    for i in range(1,len(x)-1):
        if (x[i-1]) > x[i] and x[i] < (x[i +1]):
            valleys.update({i : x[i]})  
    return list(valleys.keys())


def peaks_and_valleys(x):
   return sorted(peaks(x) + valleys(x))
    
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#print(peaks(data))
#print(valleys(data))
#print(peaks_and_valleys(data))

def visualization(x):
    l = max(x)
    while l > 0:
        for i in range(len(x)):
            if x[i]< l:
                print(" ", end=" ")
            elif x[i] == l:
                print("x", end=" ")
            elif x[i] > l:
                print("x",end=" ")
        print()
        l -= 1   

visualization(data)