def max_sum(arr,k):
    max_sum = 0

    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]

        if i >= k:
            window_sum -= arr[i-k]

        if i >= k-1:
            if window_sum > max_sum:
                max_sum = window_sum
    return max_sum
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum(arr,k))
