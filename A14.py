def duplicate_num(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 2:
            return arr[i]

arr = [1, 3, 4, 2, 2]
print(duplicate_num(arr))
