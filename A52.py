def frequency_count(arr):
    count = {}

    for i in range(len(arr)):
        if arr[i] not in count:
            count[arr[i]] = 1
        else:
            count[arr[i]] += 1
    return count
arr = [4, 2, 4, 5, 2, 4, 7, 5]
print(frequency_count(arr))
