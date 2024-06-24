def merge_sort(arr, key: str, descending: bool = False):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_lists(left, right, arr, key, descending)

def merge_two_sorted_lists(a,b,arr, key: str, descending: bool = False):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if descending:
            if a[i][key] <= b[j][key]:
               arr[k] = b[j]
               j+=1
            else:
               arr[k] = a[i]
               i+=1
        else: # ascending
            if a[i][key] <= b[j][key]:
               arr[k] = a[i]
               i+=1
            else:
               arr[k] = b[j]
               j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
        arr = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        ]
        merge_sort(arr, 'time_hours', True)
        print(arr)
        merge_sort(arr, 'name')
        print(arr)
