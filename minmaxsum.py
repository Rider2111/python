#this is the soultion of the problem from hackerrank
arr = [2,1,4,5,3]
x= len(arr)

for i in range(x - 1):  
    for j in range(x - 1 - i):  
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
minsum=0
maxsum = 0
for i in range(4):
    minsum = minsum + arr[i]

for i in range(1,5):
    maxsum = maxsum + arr[i]

print(minsum, maxsum)



