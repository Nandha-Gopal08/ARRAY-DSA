def sec_small(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[1]n
arr = [10, 5, 20, 3, 15]
print(sec_small(arr))



