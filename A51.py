def first_duplicate(arr):
    seen = set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return arr[i]
        else:
           seen.add(arr[i]) 
arr = [5, 3, 7, 2, 3, 9, 5]
print(first_duplicate(arr))
