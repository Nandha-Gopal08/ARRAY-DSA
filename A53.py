def most_frequent_element(arr):
    count = {}

    for i in range(len(arr)):
        if arr[i] not in count :
            count[arr[i]] = 1
        else:
            count[arr[i]] += 1
    max_value = 0
    max_key = None
    for key,value in count.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
arr = [1, 3, 2, 3, 4, 3, 2, 1]
print(most_frequent_element(arr))
