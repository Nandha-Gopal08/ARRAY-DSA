def subsequence(arr,sub):
    check = []
    for i in range(len(arr)):
        if arr[i] in sub:
            check.append(arr[i])
    return check == sub
arr = [1, 2, 3, 4, 5]
sub = [2, 5, 4]
print(subsequence(arr,sub))
