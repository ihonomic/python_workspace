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
    Given an array of buildings height & direction (EAST or WEST), return indices of the the houses that can see the sun
    without any other blocking its view.
    e.g: building = [3,5,4,4,3,13,2] direction = "EAST" -> [1,3, 6,7]
"""