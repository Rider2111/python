#this code is also about the problem from hackerrank, it is about sorting the items using count sorting algorrithm

arr = [1,1,3,2,1]
x=4
freq = [0] * x
for i in range(x):
    freq[i] = arr.count(i)

print(arr)
print(freq)