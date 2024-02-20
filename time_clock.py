import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
var = time.strftime('%H')

if (int(var) < 12):
    print("Good Morning!!!")
    print("Time is ",timestamp)
elif (int(var)<5):
    print("Good Afternoon")
    print("Time is ",timestamp)
elif (int(var)<8):
    print("Good Evening!")
    print("Time is ",timestamp)
else:
    print("Good Night")
    print("Time is ",timestamp)