import time
import math
from pprint import pprint
from typing import Container
#   Codewars Chanledge
""" Question: Complete the function that takes an
unsigned 32 bit number and returns a string representation of its IPv4 address."""


def int32_to_ip(int32):
    # convert to binary, convert to ip
    operand = int32
    remains = []
    while operand > 1:
        remains.append(str(operand % 2))
        operand = operand // 2
    remains.append(str(operand))
    remains.reverse()
    # print(''.join(remains))
    return ''.join(remains)


def int32_to_ip_(int32):
    # print('{:032b}'.format(int32))
    return '{:032b}'.format(int32)


int32_to_ip(128)
int32_to_ip_(128)

#   Codewars Chanledge
""" Question: Human readable time duration format """


def format_duration(seconds):
    if not seconds:
        return 'now'
    year, seconds_ = divmod(seconds, 365*24*60*60)
    month, seconds_ = divmod(seconds_, 30*24*60*60)  # This was not needed
    day, seconds_ = divmod(seconds_, 24*60*60)
    hour, seconds_ = divmod(seconds_, 60*60)
    minute, seconds_ = divmod(seconds_, 60)

    time = {"year": year, "day": day,
            "hour": hour, "minute": minute, "second": seconds_}
    my_dict = {}
    #   Check for plural
    [my_dict.update({f"{k}s,": v}) if v > 1 else my_dict.update(
        {f'{k},': v}) for k, v in time.items()]

    #   Filter the list of 0zeros
    lst = [f'{v} {k}' for k, v in my_dict.items() if v > 0]

    if len(lst) > 1:
        #   Remove the last comma and include "and"
        newWordWithoutComma = ''.join(list(lst[-2])[:-1])
        lst.remove(lst[-2])
        lst.insert(-1, newWordWithoutComma)
        lst.insert(-1, 'and')
    # print(" ".join(lst)[:-1])
    return " ".join(lst)[:-1]


format_duration(1)
format_duration(62)
format_duration(120)
format_duration(3600)
format_duration(3662)

#   Codewars chanledge
'''
Question: Soduku
'''


def check_col(board):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    col1 = [board[0][0], board[1][0], board[2][0],
            board[3][0], board[4][0], board[5][0],
            board[6][0], board[7][0], board[8][0]]
    col1.sort()

    col2 = [board[0][1], board[1][1], board[2][1], board[3][1],
            board[4][1], board[5][1], board[6][1], board[7][1], board[8][1]]
    col2.sort()

    col3 = [board[0][2], board[1][2], board[2][2], board[3][2],
            board[4][2], board[5][2], board[6][2], board[7][2], board[8][2]]
    col3.sort()

    col4 = [board[0][3], board[1][3], board[2][3], board[3][3],
            board[4][3], board[5][3], board[6][3], board[7][3], board[8][3]]
    col4.sort()

    col5 = [board[0][4], board[1][4], board[2][4], board[3][4],
            board[4][4], board[5][4], board[6][4], board[7][4], board[8][4]]
    col5.sort()

    col6 = [board[0][5], board[1][5], board[2][5], board[3][5],
            board[4][5], board[5][5], board[6][5], board[7][5], board[8][5]]
    col6.sort()

    col7 = [board[0][6], board[1][6], board[2][6], board[3][6],
            board[4][6], board[5][6], board[6][6], board[7][6], board[8][6]]
    col7.sort()

    col8 = [board[0][7], board[1][7], board[2][7], board[3][7],
            board[4][7], board[5][7], board[6][7], board[7][7], board[8][7]]
    col8.sort()

    col9 = [board[0][8], board[1][8], board[2][8], board[3][8],
            board[4][8], board[5][8], board[6][8], board[7][8], board[8][8]]
    col9.sort()
    # print([col1, col2, col3, col4, col5, col6, col7, col8, col9])
    if col1 != numbers:
        return "Bad"

    elif col2 != numbers:
        return "Bad"

    elif col3 != numbers:
        return "Bad"

    elif col4 != numbers:
        return "Bad"

    elif col5 != numbers:
        return "Bad"

    elif col6 != numbers:
        return "Bad"

    elif col7 != numbers:
        return "Bad"

    elif col8 != numbers:
        return "Bad"

    elif col9 != numbers:
        return "Bad"

    else:
        return "Good"


def check_row(board):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row1 = board[0]
    row1.sort()

    row2 = board[1]
    row2.sort()

    row3 = board[2]
    row3.sort()

    row4 = board[3]
    row4.sort()

    row5 = board[4]
    row5.sort()

    row6 = board[5]
    row6.sort()

    row7 = board[6]
    row7.sort()

    row8 = board[7]
    row8.sort()

    row9 = board[8]
    row9.sort()

    # print([row1, row2, row3, row4, row5, row6, row7, row8, row9])

    if row1 != numbers:
        return "Bad"

    elif row2 != numbers:
        return "Bad"

    elif row3 != numbers:
        return "Bad"

    elif row4 != numbers:
        return "Bad"

    elif row5 != numbers:
        return "Bad"

    elif row6 != numbers:
        return "Bad"

    elif row7 != numbers:
        return "Bad"

    elif row8 != numbers:
        return "Bad"

    elif row9 != numbers:
        return "Bad"

    else:
        return "Good"


def check_regions(board):
    #   region1
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]

    for i in col1:
        if i in col2:
            return "Bad"


def done_or_not(board):  # board[i][j]
    result3 = check_regions(board)
    result = check_col(board)
    result2 = check_row(board)

    if result == "Bad" or result2 == "Bad" or result3 == "Bad":
        return "Try again!"
    else:
        return "Finished!"


done_or_not(
    [
        [1, 3, 2, 5, 7, 9, 4, 6, 8],
        [4, 9, 8, 2, 6, 1, 3, 7, 5],
        [7, 5, 6, 3, 8, 4, 2, 1, 9],
        [6, 4, 3, 1, 5, 8, 7, 9, 2],
        [5, 2, 1, 7, 9, 3, 8, 4, 6],
        [9, 8, 7, 4, 2, 6, 5, 3, 1],
        [2, 1, 4, 9, 3, 5, 6, 8, 7],
        [3, 6, 5, 8, 1, 7, 9, 2, 4],
        [8, 7, 9, 6, 4, 2, 1, 5, 3],

    ]
)

done_or_not(
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
)

#   Codewars chanledge


def remov_nb(n):
    n = [i for i in range(n)]
    #   Choosed 2 numbers
    a, b = 15, 21

    index1 = n.index(15)
    index2 = n.index(21)

    prod = a*b
    sumn = sum([i for i in n if i != a or i != b])

    # print(prod, sumn)

    return []


remov_nb(26)

'''
    QUESTION: Table printer
'''


def printTable(data):
    ...


printTable(
    [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]
)

#   Codewars Example


def check_parathensis(string):
    string = [char for char in string if char in '()']
    o = string.count('(')
    c = string.count(')')
    if o == c:
        newList = []
        for i in string:
            if i == '(':
                newList.append(i)
            elif i == ')':
                no = newList.count('(')
                nc = newList.count(')')
                if no == nc:
                    # print("False")
                    return False
                newList.append(i)
        # print("True")
        return True
    else:
        # print('False')
        return False


check_parathensis("hi())(")
# check_parathensis("hi(hi)()")


def checkWords(word, words):
    if word not in words:
        words.append(word)
    for string in words:
        # Aviod checking itself

        print(string)


checkWords('aabb', ['aabb'])
print("+++++++++++++++++++++++++++++++++++++++++=")


# print(list(map(lambda x: ''.join(sorted(x)), ["bcadef", "ppla"])))


def anagrams(word, words=[]):
    # if word not in words:
    #     words.append(word)
    # words = ['abba', 'bbaa', 'aaab', 'baaa', 'xxxx', 'posd']
    # words = ['aabb', 'abcd', 'bbaa', 'dada', 'abba']
    # words = ['crazer', 'carer', 'racar', 'caers', 'racer']

    container = []
    anagramic = []
    for word in words:
        if ''.join(sorted(word)) in list(map(lambda x: ''.join(sorted(x)), container)):
            print("Anagram found")
            #   Get that word already in the container
            for containerWord in container:
                print(container)
                if ''.join(sorted(containerWord)) == ''.join(sorted(word)):
                    anagramic.append(containerWord)

            # append the found word
            anagramic.append(word)
            container.append(word)
        else:
            print("No anagram")
            container.append(word)

    print("anagramic=>", anagramic)
    return anagramic


# anagrams("racer", ['crazer', 'carer', 'racar', 'caers', 'racer'])
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
