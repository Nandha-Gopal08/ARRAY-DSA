def even_sum_i(arr):
    Sum = 0
    for i in range(1,len(arr),2):
        Sum += arr[i]
    return Sum
arr = [10, 20, 30, 40, 50, 60]
print(even_sum_i(arr))
