def missing_num(arr):
    expect_value = arr[0]
    for i in range(len(arr)):
        if arr[i] == expect_value:
            expect_value += 1
        else:
            return expect_value 
        
arr = [1, 2, 4, 5, 6]
print(missing_num(arr))
