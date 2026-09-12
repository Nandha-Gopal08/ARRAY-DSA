def partition(arr,pivot):
    left = 0
    right = len(arr) -1
    while(left <= right):
        while(left <= right and arr[left] < pivot):
            left += 1
        while(left <= right and arr[right] >= pivot):
            right -= 1
        if left <= right:
            arr[left],arr[right] = arr[right],arr[left]

            left += 1
            right -= 1
    return arr
arr = [9, 12, 3, 5, 14, 10, 2]
pivot = 10
print(partition(arr,pivot))
