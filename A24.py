def first_occur(arr,target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
arr = [5, 2, 8, 2, 9, 2]
target = 2
print(first_occur(arr,target))
