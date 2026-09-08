def two_sum(arr,target):
    left = 0
    right = len(arr) - 1
    while( left < right ):
        if arr[left] + arr[right] == target and left != right :
            return left,right
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1
arr = [1, 2, 7, 15]
target = 9
print(two_sum(arr,target))
