""" Question 1 - Minimum waiting time
    Given an array of time that certain queries takes to execute. Note Only one query can be execute at a time,
    but any can be executed in any order

    - A query waiting time is the amount of time that it must wait before its executions starts
    Write a function that returns the minimum amount of total waiting time to  execute all the queries
    e.g queries=[3,2,1,2,6], --> 17
    Before any of the query can be excecuted, its dependent on the sum of the queries before it. 
    Method : (nlogn) time | 0(1) space
        - Since u want the minimum queries first, sort it, then add the previous sum to the current running sum
"""


def minimumWaitingTime(queries):
    """
    Sort it
    [1,2,2,3,6]
    //  before query 1 can execute, it needs to wait for: 1 secs
    //  before query 2 can execute, it needs to wait for: 1+2 secs
    //  before query 3 can execute, it needs to wait for: 1+2+2 secs
    //  before query 4 can execute, it needs to wait for: 1+2+2+3 secs
    """
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
    A tandem bicycle is pedalled by two people, but the person that pedals faster dictates the speed of the bicycle.
    If A pedals at the rate of 5, and B pedals at the rate of 4. Bicycle speed = 5
    Given 2 teams of arrays (same length) of riders, and a fastest flag. If fastest == True, return the maximum total
    tandem speed, otherwise return the minimum total speed  
    e.g : redShirtSpeeds=[5, 5, 3, 9, 2] blueShirtSpeeds=[3, 6, 7, 2, 1] fastest=True --> 32
    Method 1: 0(nlogn) time | 0(1) time
        - To obtain the maximum = sum the maximum of each idx from both array
        - To obtain the minimum = sum the maximum and the reverse minimum. Why does one has to be reverse? To cause a 
        big gap.
"""


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    return sum(max(red, blue) for red, blue in zip(redShirtSpeeds, blueShirtSpeeds))


""" Question 4 - Task Assignments
    Given k-number of workers & an even array of tasks durations. Each worker is expected to complete 2 tasks, 
    return the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible.
    
    Your function should return a list of pairs, where each pair stores the indices of the tasks that should be
     completed by one worker.  
    e,g : k=3 tasks=[1, 3, 5, 3, 1, 4] --> 
    [
        [0,2],
        [4,5]
        [1,3]
    ]
    Method 1: 0(nlogn) time | 0(n) space
         Returns the optimal assignment of tasks.
        Avoid pairing long tasks together. Pair the shortest-duration tasks with the longest-
        duration tasks'. It would make sense to pair one low tasks with a higher one
        start by remembering the original indices of tasks.
        sort the tasks array in ascending order.
"""


def taskAssignment(k, tasks):

    tasksPairIndices = [(idx, task) for idx, task in enumerate(tasks)]

    tasksPairIndices.sort(key=lambda item: item[1])

    # the lowest duration tasks are at the beginning & the largest at the end
    # so pair them. It would make sense to pair one low tasks with a higher one
    pairTasksResult = []
    leftIdx, rightIdx = 0, len(tasksPairIndices) - 1
    while leftIdx < rightIdx:
        pairTasksResult.append(
            [tasksPairIndices[leftIdx][0], tasksPairIndices[rightIdx][0]]
        )
        leftIdx += 1
        rightIdx -= 1

    return pairTasksResult


""" Question 5 - Valid starting city
    Different cities connected in circular, find a valid starting city, where your car is filled with fuel and takes you 
    to consequtives cities for refill  & later arrive at the starting city with 0 or more fuel left.
    NOTE: Your fuel must NOT be exhausted on the way.
    
    distances[i] is the distance from the next [i+1]. Last city is connected to the first 
    fuel[i] is the total fuel available at city[i]
    mpg(mile per gallon) is the total number of miles your car can travel per gallon of fuel 
    Return the index of the valid starting city. 
    
    e.g: distances=[5, 25, 15, 10, 15] fuel=[1, 2, 1, 0, 3] mpg=10  --> 4
    
    Method 1: 0(n^2) time | 0(1) space
    Method 2: 0(n) time | 0(1) space
        The trick here,:  start at the city where you'll have the most minimum amount of gas. 
        By intuition, a more valid starting city is that after the city with the most scarcity of fuel
        From our example, city 3 has no fuel. So it's best to start at city 4. Which will be more logical to gather 
        enough fuel from other city to overcome the most  scarce city before reaching the starting point city. 
            - So as soon as we find the most scarce city [i], the next city [i+1] is the valid starting city
"""


def validStartingCity(distances, fuel, mpg):
    # 0(n) time | 0(1) space
    currentSum = 0
    mostNegativeCity = 0
    validStartingIdx = 0  # this is set to the index after the most negative sum
    for idx in range(len(distances)):
        currentSum += fuel[idx] * mpg - distances[idx]
        if currentSum < mostNegativeCity:
            mostNegativeCity = currentSum
            validStartingIdx = (idx + 1) % len(distances)
    return validStartingIdx
