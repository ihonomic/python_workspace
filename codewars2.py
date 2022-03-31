
import re

# Chanllege 1
"""
Input: words = ["today","is","friday","friday","is","the","best","day","of", "week","weekend", "doesnot", "have", "the", "friday"], k = 3
 'friday' - 3 , 'is' -> 2, 'the' -> 2
Output: ["friday","is", "the"]
"""


def num_of_occurence(words, k):
    sorted_words = [word for word in sorted(words)]

    count = {}
    for i in sorted_words:
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1

    sorted_dict = {}
    sorted_keys = sorted(count, key=count.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = count[w]

    returned_list = []
    sliced_dict = dict(list(sorted_dict.items())[:k])

    for k, v in sliced_dict.items():
        returned_list.append(k)

    print(returned_list)
    return returned_list


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
