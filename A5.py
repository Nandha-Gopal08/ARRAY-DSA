def pos_neg(arr):
    positive = 0
    negative = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
    return positive,negative 
arr = [2, -5, 7, -3, 0, 8, -1]
print(pos_neg(arr))
