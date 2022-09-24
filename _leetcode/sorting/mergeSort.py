""" Merge sort. Create One sorted array from 2 sorted Array
    
     Method : Recursively, 
            1. get middle,
            2. sort left, sort right - Recursive
            3. Merge left & right - Merge two sorted lists
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted(left, right, arr)


def merge_two_sorted(a, b, arr):

    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1

        k += 1

    #   when one list has been exhuasted
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    merge_sort(arr)
    print(arr)
