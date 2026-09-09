def last_occur(arr,target):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == target:
            return i
arr = [5, 2, 8, 2, 9, 2]
target = 2
print(last_occur(arr,target))
