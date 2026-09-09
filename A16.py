def insert_element(arr):
    value = int(input("enter element to insert"))
    index = int(input("enter index to insert "))

    arr.append(None)
    for i in range(len(arr)-1,index,-1):
        arr[i] = arr[i-1]
    arr[index] = value
    return arr
arr = [10, 20, 30, 40]
print(insert_element(arr))
