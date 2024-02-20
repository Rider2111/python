#this is a hackerrank problem to find the difference b/w the sum of diagonals of a square matrix

# matrix = [
#     [1,2,3,],
#     [4,5,6,],
#     [7,8,9,],
# ]
matrix = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]

x= len(matrix)
sum1=0
sum2=0
for i in range(x):
    for j in range(x):
        if i==j:
            sum1 +=matrix[i][j]
        # elif (i+j) == (x-1):
        #     sum2 = sum2 + matrix[i][j]
for i in range(x):
    for j in range(x):
        if (i+j) == (x-1):
            sum2 += matrix[i][j]

    
print(sum1,sum2)
diff = sum1 - sum2
print(diff)
print(abs(diff))
