def Two_Sum(arr,target):
    seen = {}
    for i in range(len(arr)):

        needed = target - arr[i]

        if needed in seen:
            return [seen[needed],i]

        seen[arr[i]] = i
arr = [6, 4, 3, 9, 2]
target = 11
print(Two_Sum(arr,target))
