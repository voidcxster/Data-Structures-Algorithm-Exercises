# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def lomutoQuickSort(elements: list[int], start: int, end: int) -> None:
    if start < 0 or end < 0:
        return
    if start > end: # TODO figure out why start values can be below end values at all
        return
    pivotIdx: int = end
    pivotVal: int = elements[pivotIdx]

    greaterIdx: int = start
    while True:
        while greaterIdx < end and elements[greaterIdx] < pivotVal:
            greaterIdx += 1

        lesserIdx: int = greaterIdx
        while lesserIdx < end and elements[lesserIdx] > pivotVal:
            lesserIdx += 1
        # print(f'greater: {greaterIdx}, lesser: {lesserIdx}')
        swap(greaterIdx, lesserIdx, elements)
        if lesserIdx == end:
            break
    # print(f'\nLeftSide\nElements: {elements}, Pivot: {pivotIdx}, Start: {start}, End: {end}, greaterIdx: {greaterIdx}')
    lomutoQuickSort(elements, start, greaterIdx - 1)
    # print(f'\nRightSide\nElements: {elements}, Pivot: {pivotIdx}, Start: {start}, End: {end}, greaterIdx: {greaterIdx}')
    lomutoQuickSort(elements, greaterIdx + 1, end)
    # elements = [11,9,29,7,2,15,28]
    # 11 9 7 29 2 15 28
    # 11 9 7 2 29 15 28
    # 11 9 7 2 15 29 28
    # 11 9 7 2 15 28 29
    # 2 9 7 11 15 28 29
    # 2 7 9 11 15 28 29
    # solution 2 7 9 11 15 28 29

# def lomutoQuickSort(elements: list[int], start: int, end: int) -> None:
#     if start < 0 or end < 0:
#         return
#
#     pivotIdx: int = end
#     pivotVal: int = elements[pivotIdx]
#
#     while True:
#         greaterIdx: int = start
#         while greaterIdx < len(elements) - 1 and elements[greaterIdx] < pivotVal:
#             greaterIdx += 1
#
#         lesserIdx: int = greaterIdx
#         while lesserIdx < len(elements) - 1 and elements[lesserIdx] > pivotVal:
#             lesserIdx += 1
#         print(f'greater: {greaterIdx}, lesser: {lesserIdx}')
#         swap(greaterIdx, lesserIdx, elements)
#         if lesserIdx == end:
#             break

    # elements = [11,9,29,7,2,15,28]
    # 28, 15, 2, 7, 29, 9, 11
    # 2 15 28 7 29 9 11
    # 2 7 28 15 29 9 11
    # 2 7 9 15 29 28 11
    # 2 7 9 11 29 28 15
    # 2 7 9 11 15 28 29


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    # for elements in tests:
    #     quick_sort(elements, 0, len(elements)-1)
    #     print(f'sorted array: {elements}')

    print('Lomuto Partition Method:\n')
    for elements in tests:
        lomutoQuickSort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')

