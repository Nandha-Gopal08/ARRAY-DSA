def compare_array(arr1,arr2):
    i = 0
    j = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] != arr2[j]):
            return False
        i += 1
        j += 1
    return True
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(compare_array(arr1,arr2))
