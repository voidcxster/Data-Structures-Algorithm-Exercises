# 1) Because the array isn't sorted. The program finds that 9 > 5, so it searches in the left where it won't find 5

# 2) Find index of all occurences of a number from sorted list 

# numbers: list[int] = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
# numbers: list[int] = [1, 2, 4, 8, 10]
numbers: list[str] = ['a', 'b', 'b', 'b', 'c']
number_to_find: int = 34

def binarySearch(array: list[int] | list[str], searchTerm: int | str) -> set[int]:
    leftBound: int = 0
    rightBound: int = len(array) - 1
    midIdx: int = (leftBound + rightBound) // 2
    foundIdx: int = -1
    foundIndexes: set[int] = set()

    while leftBound <= rightBound:
        midValue: int | str = array[midIdx]
        if midValue == searchTerm:
            foundIdx = midIdx
            break
        elif midValue > searchTerm:
            rightBound = midIdx - 1
        else:
            leftBound = midIdx + 1

        midIdx = (leftBound + rightBound) // 2

    if foundIdx == -1:
        return foundIndexes

    # check left for num
    currentIdx: int = foundIdx
    currentVal: int | str = array[currentIdx]
    while currentVal == searchTerm:
        foundIndexes.add(currentIdx)
        currentIdx -= 1
        if currentIdx < 0:
            break
        currentVal = array[currentIdx]

    # check right for num
    currentIdx = foundIdx
    currentVal = array[currentIdx]
    while currentVal == searchTerm:
        foundIndexes.add(currentIdx)
        currentIdx += 1
        if currentIdx >= len(array):
            break
        currentVal = array[currentIdx]

    return foundIndexes

# test solution
for num in numbers:
    print(binarySearch(numbers, num))
string1: int | str = 'z'
string2: str | int = 'aa'
if string1 > string2:
    print('yes')
else:
    print('no')
