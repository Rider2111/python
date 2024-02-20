def counting_sort(arr):
    # Find the minimum and maximum values in the input list
    min_val = min(arr)
    max_val = max(arr)

    # Create the counting array
    counting_array = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element
    for num in arr:
        counting_array[num - min_val] += 1
    print(counting_array)
    # Calculate cumulative counts
    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]
    print(counting_array)
    # Build the sorted output
    sorted_array = [0] * len(arr)
    for num in reversed(arr):
        sorted_array[counting_array[num - min_val] - 1] = num
        counting_array[num - min_val] -= 1

    return sorted_array

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())  
    student_data = (name, score)
students.append(student_data)