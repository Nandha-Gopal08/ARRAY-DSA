def max_subarray(arr):
    no_delete = arr[0]
    one_delete = float('-inf')
    answer = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]

        one_delete = max(
            one_delete + num,
            no_delete
        )

        no_delete = max(
            num,
            no_delete + num
        )

        answer = max(answer, no_delete, one_delete)

    return answer


arr = [1, -2, 0, 3]
print(max_subarray(arr))
