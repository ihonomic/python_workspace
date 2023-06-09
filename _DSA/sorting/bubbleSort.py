""" Bubble sort  - It's called bubble because the larger element goes to the end 
    Comparing two adjacents elements and swapping. 
    - It happens (length-1) times
    
    (time, space) = 0(n^2), 0(1)
    - DOESn't Maintain Order 
"""


def bubble_sort(elements):
    size = len(elements)

    # Flag to break out of the loop if there was no swapping. i.e it is already sorted. 0(n)
    swapped = False

    for i in range(size - 1):
        for j in range(size - 1 - i):  # stop it, because larger elements are already sorted
            if elements[j] > elements[j+1]:
                elements[j+1], elements[j] = elements[j], elements[j+1]

                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)

    print(elements)
