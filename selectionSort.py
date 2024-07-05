# def selection_sort(arr: list[dict[str, str]], keyPreference: list[str]):
#     size = len(arr)
#     for key in reversed(keyPreference):
#         for i in range(size-1):
#             min_index = i
#             for j in range(min_index+1,size):
#                 if arr[j][key] < arr[min_index][key]:
#                     min_index = j
#             if i != min_index:
#                 arr[i], arr[min_index] = arr[min_index], arr[i]
#
#             print(f'iterator: {i}')
#             printFormatted(arr)
#         print(key)
#         printFormatted(arr)

def selection_sort(arr: list[dict[str, str]], keyPreference: list[str]) -> None:
    size: int = len(arr)
    for i in range(size-1):
        min_index: int = i
        for j in range(min_index+1,size):
            for key in keyPreference:
                if arr[j][key] < arr[min_index][key]:
                    min_index = j
                    break
                elif arr[j][key] > arr[min_index][key]:
                    break
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    printFormatted(arr)

# def selection_sort(arr: list[dict[str, str]], keyPreference: list[str]) -> None:
#     size: int = len(arr)
#     key: str = keyPreference.pop(0)
#     for i in range(size-1):
#         min_index = i
#         for j in range(min_index+1,size):
#             if arr[j][key] < arr[min_index][key]:
#                 min_index = j
#         if i != min_index:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#
#         print(f'iterator: {i}')
#         printFormatted(arr)
#
#     # create arrays out of the dicts with the same value for a given key
#     arrSlice: list[dict[str, str]] = []
#     prevValue: str = arr[0][key]
#     arrSorted: list[dict[str, str]] = []
#     for elem in arr:
#         if elem[key] == prevValue:
#             arrSlice.append(elem)
#             prevValue = elem[key]
#         else:
#             arrSorted += selection_sort(arrSlice, keyPreference)
#             arrSlice.clear()
#
#     print(key)
#     printFormatted(arr)

def printFormatted(arr: list[dict[str, str]]) -> None:
    output: str = '[\n' # ]
    for idx, elem in enumerate(arr):
        output += '    ' + str(elem)
        output += ',\n' if idx != len(arr) - 1 else '\n'
    output += ']'
    print(output)

""" EXPECTED OUTPUT:
[
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    {'First Name': 'Armaan', 'Last Name': 'Dadra'}
    {'First Name': 'Armaan', 'Last Name': 'Kumar'}
    {'First Name': 'Ingrid', 'Last Name': 'Galore'}
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'}
    {'First Name': 'Jade', 'Last Name': 'Canary'}
    {'First Name': 'Jaya', 'Last Name': 'Seth'}
    {'First Name': 'Jaya', 'Last Name': 'Sharma'}
    {'First Name': 'Karan', 'Last Name': 'Kumar'}
    {'First Name': 'Kiran', 'Last Name': 'Kamla'}
    {'First Name': 'Raj', 'Last Name': 'Nayyar'}
    {'First Name': 'Raj', 'Last Name': 'Sharma'}
    {'First Name': 'Raj', 'Last Name': 'Thakur'}
    {'First Name': 'Suraj', 'Last Name': 'Sharma'}
]
"""


if __name__ == '__main__':
    names: list[dict[str, str]] = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
    selection_sort(names, ['First Name' , 'Last Name'])
    printFormatted(names)
