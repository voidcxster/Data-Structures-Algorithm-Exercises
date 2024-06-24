def insertion_sort(elements: list[int]) -> None:
    try:
        print(f'Median for [{elements[0]}]: {elements[0]}')
        for i in range(1, len(elements)):
            anchor = elements[i]
            j = i - 1
            while j>=0 and anchor < elements[j]:
                elements[j+1] = elements[j]
                j = j - 1
            elements[j+1] = anchor
            if i % 2 == 1: # even # of elements
                median: float | int = (elements[i // 2] + elements[i // 2 + 1]) / 2
                if median == int(median): # only zeroes after decimal, can safely convert to int w/o rounding
                    median = int(median)
            else: # odd
                median: float | int = elements[i // 2]
            print(f'Median for {elements[0:i + 1]}: {median}')
    except IndexError:
        pass # do nothing for empty list

if __name__ == '__main__':
    elements: list[int] = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print(elements)

    tests: list[list[int]] = [
        [2, 1, 5, 7, 2, 0, 5],
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        unsortedElements: list[int] = elements.copy()
        insertion_sort(elements)
        print(f'sorted array for {unsortedElements}: {elements}')
