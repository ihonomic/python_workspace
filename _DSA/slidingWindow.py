from collections import deque
#   MAXIMUM SLIDING WINDOW


def maximumSlidingWindow(arr, k):
    ''' 
    - Return an array of the maximum element for each range of k-window
    arr = [8,3,-1,-3,5,3,6,7] k = 3
    result = [8, 3, 5, 5, 6, 7]
    '''
    #   METHOD 1
    """ Slice k size and find the max """

    left, right = 0, len(arr)-1
    res = []

    while left <= right-k+1:
        slide = arr[left:left+k]
        m = max(slide)
        res.append(m)
        left += 1
    return res

    #  METHOD 2 - Using Deque
    """ Keep indexes of the elements larger than the previous in a deque, Maintain k size. """

    d = deque()
    res = []
    for i, n in enumerate(arr):

        while d and n >= arr[d[-1]]:
            d.pop()  # Remove last element if current element is greater than the last

        d.append(i)  # keep the index

        # compute if current index is equal to k '
        if i + 1 >= k:
            res.append(arr[d[0]])

        # remove last element if current index is more than k
        if i - d[0]+1 == k:
            d.popleft()

    return res


print(maximumSlidingWindow([8, 3, -1, -3, 5, 3, 6, 7], 3))
