def del_element(arr):
    index = int(input("enter the index to delete an element : "))

    for i in range(index,len(arr)-1):
        arr[i] = arr[i+1]
    n = len(arr) - 1

    return arr[:n]
arr = [10, 20, 30, 40, 50]
print(del_element(arr))
