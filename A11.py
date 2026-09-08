def duplicates(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] not in res:
            res.append(arr[i])
    return res
arr = [1, 2, 2, 3, 4, 4, 5]
print(duplicates(arr))
