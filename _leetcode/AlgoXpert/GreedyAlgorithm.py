""" Question 1 - Minimum waiting time
    Given an array of time that certain queries takes to execute. Note Only one query can be execute at a time,
    but any can be executed in any order

    - A query waiting time is the amount of time that it must wait before its executions starts
    e.g queries=[3,2,1,2,6], --> 17
    Method : (nlogn) time | 0(1) space
        - Since u want the minimum queries first, sort it, then add the previous sum to the current running sum
"""


def minimumWaitingTime(queries):
    queries.sort()

    runningSum = 0
    prevSum = 0

    for time in queries:
        runningSum += prevSum
        prevSum += time
    return runningSum


""" Question 2 - Class Photos
    You're a photographer sent to a class of even number of students where half of them is wearing blue & the otherhalf 
     wearing red shirts. You need to arrange the students in 2 rows before snapping. Each row should be of the same len
     and:
        - All students wearing shirt red should be in one row, and same for those wearing blue
        - Each students in the backrow must be strictly taller that those in the front row
    e.g redShirtHeights=[5,8,1,3,4], blueShirtHeights=[6,9,2,4,5] --> True. // All students with blue shirts at the back
    Method 1: 0(nlogn) time | 0(1) space 
        - Sort the arrays, Use the tallest student to know if red or blue should be at the back row
        - If at any point, the backrow students is not taller than the frontrow student return False
"""


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    tallestRed = redShirtHeights[0]
    tallestBlue = blueShirtHeights[0]

    if tallestRed > tallestBlue:
        sittingOrder = zip(redShirtHeights, blueShirtHeights)
    else:
        sittingOrder = zip(blueShirtHeights, redShirtHeights)

    for backHeight, frontHeight in sittingOrder:
        if backHeight <= frontHeight:
            return False
    return True


""" Question 3 - Tandem Bicycle
    Method 1: 
"""