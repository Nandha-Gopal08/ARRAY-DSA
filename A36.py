def difference(arr1,arr2):
    res = []
    i = 0
    while(i < len(arr1)):
        if arr1[i] not in arr2:
            res.append(arr1[i])
            i +=n1
        i += 1
    return res
arr1 = [1, 2, 3, 5, 7]
arr2 = [2, 4, 5, 6]
print(difference(arr1,arr2))
