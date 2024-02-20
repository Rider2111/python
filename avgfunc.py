def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print("Average is ", (sum/len(number)))
    

average(3,4,54,2,54,7,0,1)

