def large_element(arr):
    large = 0
    for i in range(len(arr)):
        if(large < arr[i]):
            large = arr[i]
    return large
arr = [12, 5, 27, 8, 19]
print(large_element(arr))
