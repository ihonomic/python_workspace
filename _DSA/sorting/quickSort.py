""" Quick sort, 
    Selecting a pivot and sort left and right partitions, so that elements before it are lower and elements after it are higher. 
    
    [11,9,29,7,2,15,28]
    Assuming 11 is pivot, => [7,9,2,11,29,15,28]
    
    The process of putting a pivot in it's right position is called "partitioning". There are 2 types:
        1. Hoare Partition 
            p  strt         stop
            [11,9,29,7,2,15,28]
            - Uses the left most element (p).
            - start pointer is the next element after the left-most element (p)
            - end is the last. 
            * Keep moving start pointer until you find an element greater than p
            * Keep reducing end pointer until you find element less than p 
            * Swap start & end pointers
            * continue moving start pointer from the last swap location, searching for elements greater than p. 
            * Stop process when end pointer crosses start pointer. i.e start pointer becomes greater than end pointer
            * When you stop the process, swap end pointer and pivot
        2. Lomuto Partition
                  pi i      p
            [11,9,29,7,2,15,28]
            - Uses the end element as pivot (p).
            - First element is called p-index (partioning index)
            * Keep moving p-index until you find element greater than pivot
            * start another counter (i), from where p-index was found.
            * i is looking for elements less than p, if found
            * swap p-index and i 
            * KEEP MOVING p-index until it finds elements greater than pivot and i begins from that point to find element less than p for a swap
"""


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)

        quick_sort(elements, start, pi - 1)     # left partition
        quick_sort(elements, pi + 1, end)        # right partition


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)

    print(elements)
