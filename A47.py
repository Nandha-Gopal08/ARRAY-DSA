def small_subarray(arr,target):
    left = 0
    min_length = len(arr) + 1
    sum_array = 0
    for right in range(len(arr)):
        sum_array += arr[right]

        while(sum_array >= target):
            length = right - left + 1

            if length < min_length:
                min_length = length

            sum_array -= arr[left]
            left += 1
    if min_length == len(arr) + 1:
        return 0
    return min_length
arr = [2, 3, 1, 2, 4, 3]
target = 7
print(small_subarray(arr,target))
