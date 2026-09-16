def range_sum(arr,l,r):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for i in range(1,len(arr)):
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]
        
arr = [2, 4, 1, 6, 3, 5]
print("enter range sum query")
l = int(input("enter start index"))
r = int(input("enter end index"))
print(range_sum(arr,l,r))
