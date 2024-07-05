def shell_sort(arr: list[int]) -> None:
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        print(arr, gap)
        gap = gap // 2
        """
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [1, 6, 2, 7, 12, 9, 17, 23, 21, 53, 78, 61, 90] 3
        """

def shell_sort_remove_duplicates(arr: list[int]) -> None:
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            if i > size - 1:
                break
            print(arr, i)
            anchor = arr[i]
            j = i
            while j>=gap:
                if arr[j - gap] > anchor:
                    arr[j] = arr[j-gap]
                    j -= gap
                elif arr[j - gap] == anchor:
                    del arr[j - gap]
                    i -= 1
                    j -= 1
                    size -= 1
                else:
                    break
            arr[j] = anchor
        print(arr, gap)
        gap = gap // 2
        """
        2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3

        2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3 ; 6
        """

if __name__ == '__main__':
    # tests = [
    #     [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
    #     [],
    #     [1,5,8,9],
    #     [234,3,1,56,34,12,9,12,1300],
    #     [5]
    # ]
    elements: list[int] = [90,78,61,53,23,21,17,12,9,7,6,2,1]
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    elements = [1, 1, 1, 2, 3]
    shell_sort_remove_duplicates(elements)
    print(elements)
    # for elements in tests:
    #     shell_sort(elements)
    #     print(elements)
