def maximum_element(arr):
    Max = 0

    for i in range(len(arr)):
        if arr[i] > Max:
            Max = arr[i]
    return Max
arr = [12, 5, 27, 8, 19]
print(maximum_element(arr))
