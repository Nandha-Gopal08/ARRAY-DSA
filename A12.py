def move_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i,len(arr)-1):
                arr[j] = arr[j+1]
            arr[len(arr)-1] = 0
    return arr
arr = [0, 1, 0, 3, 12]
print(move_zeros(arr))
