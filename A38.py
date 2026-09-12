def specific_value(arr,target):
    slow = 0
    fast = 0
    while(fast < len(arr)):
        if arr[fast] != target:
            arr[slow] = arr[fast]
            slow += 1


        fast += 1
    return arr[:slow]
arr = [3, 2, 2, 3, 4, 2]
target = 2
print(specific_value(arr,target))
