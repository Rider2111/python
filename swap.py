#to swap two number we can use this
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

temp = x
x = y
y = temp
# another way of doing this is: 
# x , y = y, x

print("After swapping first number is ", x ,"and second number is ", y)