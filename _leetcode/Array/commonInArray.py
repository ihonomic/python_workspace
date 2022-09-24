from collections import Counter

"""
return characters present in an array of strings
"""
#   Method 1


def commonChars2(arr):

    res = Counter(arr[0])

    for word in arr[1:]:
        res &= Counter(word)

    return list(res.elements())

#   Method 2


def commonChars(arr):
    check = list(arr[0])
    for word in arr[1:]:
        repatedChar = []
        for char in word:
            if char in check:
                repatedChar.append(char)
                check.remove(char)

        check = repatedChar
    return check


# print(commonChars2(["bella", "label", "roller"])) -> ['l', 'l', 'e']
