def remove_occur(arr,target):
    slow = 0
    fast = 0
    while(fast < len(arr)):
        if(arr[fast] != target):
            arr[slow] = arr[fast]
            slow += 1


        fast += 1
    return arr[:slow]
arr = [5, 2, 3, 2, 4, 2, 6]
target = 2
print(remove_occur(arr,target))
