def sec_large(arr):
    sec_large = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr[-2]
arr = [10, 5, 20, 8, 15]
print(sec_large(arr))
