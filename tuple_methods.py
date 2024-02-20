# in this we will discuss all about tuple in python: we cannot change the value of tuple
tup = (1,4,9,0,'hi',False,0)
print(tup)
print(tup[2])
print(tup[0:2])

#all things are same as in the case of list, except that we cannot change or update the tuple

if 0 in tup:
    print("Yes, True")

''' if we want to change the values in tuple then first we have to change
that tuple into a list and the make changes and then again convert it to a tuple'''
# for making changes we can do this

animals = ('cat','dog', 'lion','cow','tiger')
temp = list(animals)
temp.append("rabit") # to add item
temp.pop(4)  # to remove an item
temp[2] = "horse"
animals = tuple(temp)
print(animals)

#although we can concatenate two tuples without converting them to list this is becaue we are creating another tuple here
animals1 = ("Deer","Elephant","Camel")
allanimals = animals + animals1
print(allanimals)

tuple1 = (3,43,54,23,0,87,67,0,0,3,1)
res = tup.count(0) #this is as same in the case of list
print(res)

#for index
res1 = tuple1.index(3)
print(res1)

res2 = tuple1.index(3, 1,10)
print(res2)