# Trie - Are super useful in finding strings, searching for strings, matching strings.

""" Question 1 - SUFFIX TREE CONSTRUCTION - Check if a string is contained in suffix on another string.
    "babc" -> "bc" -> True, "bc" appears at the suffix of main string. 
    "babc" -> "bab" -> False, "bab" appears at the preffix of main string. (You would know because it doesnt end with *`)

    Method:
    CONSTRUCTION 0(n^2) time, 0(n^2) space
    Using hash tables, if key already exists, add the current character else, create the key character
    on the root. 

                                            root
                                        /     |    \  
                                      b      a      c 
                                    / \      \       \
                                  c    a      b       *
                                /      \       \
                               *        b       c
                                        \        \
                                         c         *
                                         \
                                         *
    SEARCHING 0(n) time, 0(1) space
    {
        "b": {"a": {"b": {"c": {"*": True}}}, "c": {"*": True}},
        "a": {"b": {"c": {"*": True}}},
        "c": {"*": True},
    }
"""
# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # 0(n^2) time | 0(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]  # shift to next node
        node[self.endSymbol] = True

    # 0(n) time | 0(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]  # shift to next node
        return self.endSymbol in node


""" Question 2 - Multi String search 
  Write a func that takes in a big string and an array of small strings, all of which are smaller in length than the big 
  strings. The function should return an array of booleans, where each boolean represents whether the small string at that
  index in the array of small strings is contained in the big strings 

  NOTE: Don't use language built-in methods 
  e.g: bigString='this is a big string' smallStrings=['this', 'yo', 'is', 'a', 'bigger', 'string', 'kappa']
  --> [True, False, True, True, False, True, False]

      bigString='abcdefghijklmnopqrstuvwxyz' smallStrings=['abc', 'mnopqr', 'wyz', 'no', 'e', 'tuuv']
  --> [True, True, False, True, True, False]

  METHOD 1: 
"""


def multiStringSearch(bigString, smallStrings):
    return [True if bigString.find(string) != -1 else False for string in smallStrings]
