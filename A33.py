def intersection_arrays(arr1,arr2):
    intersection_array = []
    i = 0
    while(i < len(arr1)):
        if arr1[i] in arr2:
            intersection_array.append(arr1[i])
        i += 1
    return intersection_array
arr1 = [1, 2, 3, 4, 6]
arr2 = [2, 4, 6, 8]
print(intersection_arrays(arr1,arr2))
