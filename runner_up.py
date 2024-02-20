#this code is for a problem from hackerrank to find the second highest number from list

arr= [2,3,6,6,5]

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]<arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        print(arr[i+1])
        break

print(arr)