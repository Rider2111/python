#this program is the for the problem from hackerrank it is about 
#finding the item in array which onnly occur once

lst = [1,2,3,4,3,2,1]
#lst = [0,0,1,2,1]
#lst = [1,1,2]
#lst = [1,]

for i in lst:
    if (lst.count(i) == 1):
        print(i)

print(lst)
print(len(lst))
