def sum_even_i(arr):
    Sum = 0
    for i in range(0,len(arr),2):
        Sum += arr[i]
    return Sum
arr = [10, 20, 30, 40, 50, 60]
print(sum_even_i(arr))
