def move_even(arr):
    left = 0
    right = len(arr) - 1
    while(left < right ):
        if arr[left] % 2 == 0 and arr[right] % 2 != 0:
            arr[left],arr[right] = arr[right],arr[left]
        elif(arr[left] % 2 == 0):
            right -= 1
        else:
            left += 1
    return arr
arr = [10, 2, 8, 4, 51, 6]
print(move_even(arr))
