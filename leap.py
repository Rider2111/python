# this is for the problem i did on hackerrank
x = int(input("Enter year: "))

if (x%400==0 or (x%4==0 and x%100!=0)):
    print("true")
else:
    print("False")