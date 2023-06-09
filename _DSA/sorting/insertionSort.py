""" Insertion Sort - 

Start from the second index, compare element with the previous, 
 Continue to drill backwards, and keep swapping
"""


def insertionSort(elements):

    for i in range(1, len(elements)):  # second Index

        anchor = elements[i]

        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1

            print(j, "")
        print("*" * 10)

        elements[j+1] = anchor


if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]

    insertionSort(elements)

    print(elements)
