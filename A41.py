def remove_duplicates(arr):
    slow = 0
    fast = 1
    while(fast < len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

        fast += 1
    return arr[:slow + 1]
arr = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(arr))
