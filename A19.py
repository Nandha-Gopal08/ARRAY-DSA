def count_odd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            count += 1
    return count
arr = [1, 4, 7, 8, 11, 14]
print(count_odd(arr))
