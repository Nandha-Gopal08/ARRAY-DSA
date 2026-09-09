def min_element(arr):
    Min = arr[0]

    for i in range(len(arr)):
        if arr[i] < Min:
            Min = arr[i]
    return Min
arr = [15, 8, 22, 3, 19]
print(min_element(arr))
