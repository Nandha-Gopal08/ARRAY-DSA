def First_Non_Repeating_Element(arr):
    seen = {}
    for value in arr:
        if value not in seen:
            seen[value] = 1
        else:
            seen[value] += 1
    for key,value in seen.items():
        if value == 1:
            return key
arr = [4, 5, 1, 2, 1, 4, 5]
print(First_Non_Repeating_Element(arr))
