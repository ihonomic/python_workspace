""" Question 1 - Min Max Stack Construction
    METHOD 1:  0(1) time | 0(1) space
    Hold a list of dictionary of the last min and max,
"""


class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []  # this holds a dictionary of last computed min & max
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        if self.minMaxStack:
            lastSaved = self.minMaxStack[-1]
            newMin = min([lastSaved["min"], number])
            newMax = max([lastSaved["max"], number])
            self.minMaxStack.append({"min": newMin, "max": newMax})
        else:
            self.minMaxStack.append({"min": number, "max": number})
        return self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]


""" Question 2 - Balanced brackets (Valid parenthensis)
    Write a func that takes a strings of brackets, ({[]}) in any order, and return true or false if it is balanced
    Note: A balanced string is one that has equal opening & closing (same type) and not intercepted with the closing of 
    another type. Return False if of the same kind, the closing appears first before the opening 
    e.g : "([])(){}(())()()" --> True
    METHOD 1: 0(n) time | 0(n) space
        If its opening, append to a stack. Otherwise if closing,  and stack is empty, there is no opening
            But if closing is detected and stack not empty, check if the peek is the opening of its kind.
            Lastly, if anything remains in the stack, return False
"""


def balancedBrackets(string):
    d = {")": "(", "]": "[", "}": "{", }
    stack = []
    for s in string:
        if s in ["(", "{", "["]:
            stack.append(s)
        elif s in [")", "}", "]"]:
            if stack and stack[-1] == d[s]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


""" Question 3 - Sunset Views
    Given an array of buildings height & direction (WEST (left) or EAST (right) ), 
    return indices of the the houses that can see the sun without any other blocking its view.
    e.g: building = [3,5,4,4,3,13,2] direction = "EAST" -> [1,3, 6,7]
    METHOD  1: 0(n) time | 0(n) space
    Keep track of the highest building you've seen so far, only add building idx of those higher
"""


def sunsetViews(buildings, direction):
    idxBuildings = []
    highestBuildingSofar = 0
    n = len(buildings)

    for idx in range(n - 1, -1, -1) if direction == "EAST" else range(n):
        if buildings[idx] > highestBuildingSofar:
            idxBuildings.append(idx)
            highestBuildingSofar = buildings[idx]

    return idxBuildings[::-1] if direction == "EAST" else idxBuildings  # reverse back


""" Question 4 - Sort stack
    Recursively sort an array using a stack. Only utilize pop & append
    e.g : [-5, 2, -2, 4,3,1] -> [-5,-2,1,2,3,4]
    METHOD 1: 0(n^2) time | 0(n) space
    FRecursively pop all elements from the stack , append each element to stack and if the peak element 
    is higher than the incoming, pop it out & add the incoming. 
"""


def sortStack(stack):
    # 1. Pop out evrything
    if not len(stack):
        return stack

    top = stack.pop()

    sortStack(stack)

    # 2. From the last item popout, start inserting
    insertInsortedOrder(stack, top)

    return stack


def insertInsortedOrder(stack, value):
    if not stack or stack[-1] <= value:
        stack.append(value)
        return

    # But if the peak is higher than the incoming,
    top = stack.pop()

    insertInsortedOrder(stack, value)

    # Add it back
    stack.append(top)


""" Question 5 - Next Greater Element
    Find the next greater element
    e.g : [2, 5, -3, -4, 6, 7, 2] -> [5, 6, 6, 6, 7, -1, 5]
    METHOD 1: 0(n^2) time | 0(n) space
        Create new roundabout subarray and find the next num greater than the current num
    METHOD 2 :  0(n) time | 0(n) space
        Transverse twice. Save each element indexes in a stack
        If the element of the last saved idx in the stack is less than the current, pop it off & replace the result.
"""


def nextGreaterElement(array):
    # 0(n^2) time | 0(n) space
    res = [-1] if len(array) == 1 else []

    for idx, num in enumerate(array):
        rotatedArray = array[idx + 1:] + array[:idx]

        for i, n in enumerate(rotatedArray):
            if n > num:
                res.append(n)
                break
            elif i == len(rotatedArray) - 1:
                res.append(-1)

    return res


def nextGreaterElement(array):
    # 0(n) time | 0(n) space
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array)):
        k = idx % len(array)

        while len(stack) and array[stack[-1]] < array[k]:
            top = stack.pop()
            result[top] = array[k]

        stack.append(k)

    return result


""" Question 6 - Shorten Path
    Write a func that takes in a file path, & return the shortenened version of it.
    e.g : /foo/../test/../test/../foo//bar/./baz    -->     /foo/bar/baz
    METHOD 1: (0)n time | (0)n space
        NOTE: single period (.) and // are useless
        Split by /, Remove empty strings & . 
        start adding item to stack. Whenever, the previous item == '..', pop it out & don't add the current item
        (take note of back to back .. ) - Don't remove 
"""


def shortenPath(path):
    startsWithSlash = path[0] == "/"
    tokens = path.split("/")
    stack = []

    # remove meaningless "." & ""
    newTokens = list(filter(removePeriodAndEmptyString, tokens))

    if startsWithSlash:
        stack.append("")

    for token in newTokens:
        if token == "..":
            if not stack or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == "":
        return "/"

    return "/".join(stack)


def removePeriodAndEmptyString(token):
    return len(token) > 0 and token != "."


""" Question 7 - Largest Rectangle under skyline
    Write a func that takes in an array of positive intergers, representing the heights of adjacent buildings
    and return the area of the largest rectangle that can be created by any number of adjacent buildings. Including
    just one building. All building have the same width of 1.
    e.g: [1, 3, 3, 2, 4, 1, 5, 3, 2] --> 9
    METHOD 1: 0(n^2) time | 0(1) space
        Loop through every building, while expanding left and right, count the buildings that have the same heights or
        higher than current building. if a building with a lower height is found,  break out of the loop
        - Compare the current maximum with the previous.
    Method 2: 0(n) time | 0(n) space
"""


def largestRectangleUnderSkyline(buildings):
    maxRectangle = 0
    for idx, currentHeight in enumerate(buildings):
        countBuildings = 1  # start count from itself
        left = idx - 1
        right = idx + 1

        while left >= 0:
            if buildings[left] >= currentHeight:
                countBuildings += 1
            else:
                break
            left -= 1

        while right < len(buildings):
            if buildings[right] >= currentHeight:
                countBuildings += 1
            else:
                break
            right += 1
        maxRectangle = max(maxRectangle, countBuildings * currentHeight)
    return maxRectangle
