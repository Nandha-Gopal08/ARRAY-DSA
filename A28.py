def move_pos_neg(arr):
    left = 0
    right = len(arr) - 1
    while(left < right ):
        if arr[left] < 0 and arr[right] > 0:
            arr[left],arr[right] = arr[right],arr[left]
        elif(arr[left] < 0):
            right -= 1
        else:
            left += 1
    return arr
arr = [2, -3, 5, -1, 6, -4]
print(move_pos_neg(arr))
