def rotate_left(arr):
    store = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = store
    return arr
arr = [1, 2, 3, 4, 5]
print(rotate_left(arr))
