def small_element(arr):
    small = arr[0]
    for i in range(len(arr)):
        if small > arr[i]:
            small = arr[i]
    return small
arr = [12, 5, 27, 8, 19]
print(small_element(arr))
