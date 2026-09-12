def merge_arrays(arr1,arr2):
    merge_array = []

    i = 0
    while(i<len(max(arr1,arr2))):
          merge_array.append(arr1[i])
          merge_array.append(arr2[i])

          i += 1
    return merge_array
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge_arrays(arr1,arr2))
