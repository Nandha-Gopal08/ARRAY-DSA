def arr_sort(arr):
    check = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
            
arr = [1, 2, 3, 4, 5]
print(arr_sort(arr))
