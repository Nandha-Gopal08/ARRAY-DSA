def rotate_right(arr):
    store = arr[-1]
    for i in range(len(arr)-1,-1,-1):
        arr[i] = arr[i-1]
    arr[0] = store
    return arr
arr = [1, 2, 3, 4, 5]
print(rotate_right(arr))
