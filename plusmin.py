#this is the soultion of the problem from hackerrank
def plusMinus(arr):
    x = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for i in range(len(arr)):
        if (arr[i]>0):
            pos = pos + 1
        elif (arr[i]==0):
            zer = zer + 1
        else:
            neg = neg + 1
    ratio1 = pos/x
    
    ratio2 = neg/x
    
    ratio3 = zer/x
    
    print(f"{ratio1:.6f}")
    print(f"{ratio2:.6f}")
    print(f"{ratio3:.6f}")

arr = (4,5,0,-1,0,-5,1)
plusMinus(arr)
