def sum_nested_list(arr: list) -> int | float:
    if len(arr) == 1:
        if type(arr[0]) is list:
            return sum_nested_list(arr[0])
        else: # arr[0] is num
            return arr[0]

    if type(arr[0]) is list:
        return sum_nested_list(arr[0]) + sum_nested_list(arr[1:])
    else: # arr[0] is num
        return arr[0] + sum_nested_list(arr[1:])

if __name__ == '__main__':
    print(sum_nested_list([1, 2, 3, 4, 5]))
    print(sum_nested_list([1, 2, [3,4], [5,6]]))
