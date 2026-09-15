def move_nonZero(arr):
    slow = 0
    fast = 1
    while(fast < len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]

            slow += 1


        fast +=1
    return arr[:slow]
        
arr = [0, 3, 10, 5, 2, 9, 4]
print(move_nonZero(arr))
