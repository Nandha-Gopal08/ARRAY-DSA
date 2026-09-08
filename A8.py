def count_occurence(arr,target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count
arr = [2, 4, 2, 6, 2, 8, 4]
target = 2
print(count_occurence(arr,target))
