#this program is all about list if we use [] it will be list and if we use () it will tupple
arr = [2,32,43,123,4,45,34]
print(arr)

arr1 = [23,43,231,'hi', "hello"]
print(arr1)

#this is to check if the value is in list and same we can use in strings
if 2 in arr:  
    print("yes")
else:
    print("no")

if 'hi' in arr1:
    print("yes")
else:
    print("no")

if "2" in arr:
    print("yes")
else: 
    print("no")

#this is to make the value jump it takes values on the gap of 2
print(arr[0:5:2]) 

# list comprehension: it is a way to create a new list without using for loop and following a given condition
# new_list = [expression for item in iterable if condition]
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#list methods
lst = [23,343,1,2,0,3,0,1,1]
print(lst)

#to add something in the list
lst.append(4) 
print(lst)


# to sort
lst.sort()  
print(lst)
lst.sort(reverse=True) #to sort in descending order
print(lst)

# to reverse our original list it doesn't sort the list it just reverse our original list
lst.reverse()   
print(lst)

# to find the index of a value in the list: it only gives the index of first occurance only
print(lst.index(23))   

#to find the number of occurrences of a specific value in the list
print(lst.count(1))  

#to make a copy of list or to store a list with some other variable we use copy() function
m = lst.copy()   

# to insert some value in the list we user insert(index, vallue) function
lst.insert(3,3333)
print(lst)

#this function will extend the list1 and will add the values of another list2 in the end of list1
newlst = [300,400,500]
lst.extend(newlst)
print(lst)

# to concatenate or merge two lists: in this it does not changes the original list
lst1 = [3,42,12,0,23,4]
lst2 = [76,876,87]
k = lst1 + lst2
print(k)

