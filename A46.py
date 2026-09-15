def long_subarray(arr,target):
    length = 0
    sum_array = 0
    for i in range(len(arr)):
        sum_array += arr[i]

        if sum_array <= target:
            length += 1
            
        if sum_array > target:
            sum_array -= arr[i - length]
    return length
arr = [2, 1, 3, 2, 1]
target = 9
print(long_subarray(arr,target))
