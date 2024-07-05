def sum_list(arr: list[int | float]) -> int | float:
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_list(arr[1:])

if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4, 5]))
