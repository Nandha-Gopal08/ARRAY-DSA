def even_nums(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count += 1
    return count
arr = [1, 4, 7, 8, 10, 13, 16]
print(even_nums(arr))
