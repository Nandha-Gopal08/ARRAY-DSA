def pre_hash(arr,target):
    seen = {0:-1}
    prefix = 0

    for i in range(len(arr)):
        prefix += arr[i]

        needed = prefix - target

        if needed in seen:
            return arr[seen[needed]+1:i+1]
        seen[prefix] = i
    return []
arr = [1, 2, 3, 4, 5]
target = 9
print(pre_hash(arr,target))
