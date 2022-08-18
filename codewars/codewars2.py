
import re

# Chanllege 1
"""
Input: words = ["today","is","friday","friday","is","the","best","day","of", "week","weekend", "doesnot", "have", "the", "friday"], k = 3
 'friday' - 3 , 'is' -> 2, 'the' -> 2
Output: ["friday","is", "the"]
"""


def num_of_occurence(words, k=3):
    d = {}
    for elem in data:
        d.setdefault(elem, 0)
        d[elem] += 1
        
    sort_d = sorted(d.items(), key=lambda x: x[-1], reverse=True)

    return [k for k, v in sort_d][0:k]


words = ["today", "is", "friday", "friday", "is", "the", "best",
         "day", "of", "week", "weekend", "doesnot", "have", "the", "friday"]

# num_of_occurence(words, 3)
# ===========================


# Chanllege 2

'''
    Take out everything after special characters but end an any new line 
'''


def solution(string, markers):
    markers = [''.join(markers)]
    print(markers)

    regPattern = re.compile(r' ([$#!]|[$#!]).*')
    searchOutcome = regPattern.sub('', string)

    print(repr(searchOutcome))
    return searchOutcome


solution("apples, pears # and bananas\ngrapes\nbananas !apples",
         ["#", "!"])  # "apples, pears\ngrapes\nbananas"
solution("a #b\nc\nd $e f g", ["#", "$"])  # "a\nc\nd"
