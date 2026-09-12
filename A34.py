def common_elements(arr1,arr2):
    arr1.sort()
    arr2.sort()
    common = []
    i = 0
    j = 0
    while(i < len(arr1) and j<len(arr2)):
        if arr1[i] == arr2[j]:
            common.append(arr1[i])

            i += 1
            j += 1
        elif(arr1[i] < arr2[j]):
            i += 1
        else:
            j += 1
    return common
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 3, 5, 8, 9]
print(common_elements(arr1,arr2))
