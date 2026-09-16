def subarray_sum(arr,target):
    prefix_sum = [0]
    for i in range(1,len(arr) + 1):
        print(prefix_sum[i-1])
        prefix_sum.append(prefix_sum[i-1] + arr[i-1])
        print(prefix_sum[i])
    for i in range(1,len(prefix_sum)):
        for j in range(i):
            if prefix_sum[i] - prefix_sum[j] == target:
                return arr[j:i]
arr = [3, 4, 2, 1, 6]
target = 6
print(subarray_sum(arr,target))
