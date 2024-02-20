#this piece of code is about case in python
m = int(input("Enter the marks of the student: "))
print("Marks of the student is: ", m)

if m > 80:
    print("1st division")
elif m > 60:
    print("2nd division")
elif m > 40:
    print("3rd division")
else:
    print("Fail")
