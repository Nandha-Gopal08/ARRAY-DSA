def sum_elements(arr):
    Sum = 0

    for i in range(len(arr)):
        Sum += arr[i]
    return Sum
arr = [2, 4, 6, 8, 10]
print(sum_elements(arr))
