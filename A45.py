def min_sum(arr,k):
    min_sum = float('inf')

    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]

        if i >= k:
            window_sum -= arr[i-k]

        if i >= k-1:
            if window_sum < min_sum:
                min_sum = window_sum
    return min_sum
arr = [4, 2, 1, 6, 3, 2]
k = 2
print(min_sum(arr,k))
