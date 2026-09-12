def merge_without_duplicates(arr1,arr2):
    merge = []
    i = 0
    j = len(arr2) - 1

    while(i < len(arr1) and j >= 0):
        if(arr1[i] not in merge ):
            merge.append(arr1[i])
            i += 1
        else:
            i += 1
        if(arr2[j] not in merge):
            merge.append(arr2[j])
            j -= 1
        else:
            j -= 1
    return merge
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(merge_without_duplicates(arr1,arr2))
