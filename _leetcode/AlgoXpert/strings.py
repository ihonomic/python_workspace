""" Question 1 - Caesar Cipher Encryptor
    Given a string(lowercase) and a key(number), return a new string that has been rotated by key number of times
    e.g => 'xyz' -> 'zab'
    METHOD 1 : use python builtin functions (ord and chr)
    METHOD 2 : Create a custom list of characters
"""


def caesarCipherEncryptor(string, key):
    # 0(n) time | 0(n) space
    key = key % 26
    numbers = [ord(s) for s in string]

    for i, n in enumerate(numbers):
        numbers[i] = n + key

        if numbers[i] > 122:
            numbers[i] = 96 + (numbers[i] % 122)

        numbers[i] = chr(numbers[i])

    return ''.join(numbers)

    def caesarCipherEncryptor(string, key):
        # 0(n) time | 0(n) space
        key = key % 26
        letters = list("abcdefghijklmnopqrstuvwxyz")

        numbers = [(letters.index(s) + key) % 26 for s in string]

        for i, n in enumerate(numbers):
            numbers[i] = letters[n]

        return ''.join(numbers)


""" Question 2 - Run Length Encoding 
    Given a non-empty string, return its run-length encoding. Limits run of more than 9 consecutives alphabets
    e.g => 'AAAAAAAAAAAAABBCCCCDD' -> '9A4A2B4C2D'
    METHOD 1 : 0(n) time | 0(1) space. Start from second index, compare with the previous, count if similar, otherwise, reset count.
                Remember to concatenate the last index from the loop
"""


def runLengthEncoding(string):
    # 0(n) time | 0(1) space
    res = ''
    count = 1
    i = 0

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i-1]
        if curr == prev and count < 9:
            count += 1
        else:
            res += str(count) + prev
            count = 1
    res += str(count) + string[i]           # NOTE: Handle Last case
    return res


"""Question 3 - Given a strings of characters and string of document, 
        check if all characters of documents (inlcuding spaces) can be generated
        from the characters.
    e.g: 'Bste!hetsi ogEAxpelrt x ', 'AlgoExpert is the Best!' -> True
    METHOD 1 : 0(d) time | 0(c) space
    METHOD 2 : 0(d + c) time | 0(1) space - Count the frequency of characters in 'document' and see if it matches the number of occurrences in 'characters'
                If less, return false.
"""


def generateDocument(characters, document):
    # 0(d) time | 0(c) space
    c = list(characters)
    for i in document:
        if i in c:
            c.remove(i)
        else:
            return False
    return True


"""Question 4 - Return the index of the first non-repeating character 
    e.g: 'abcdcaf' -> 1, (since b was the first letter not to be repeated)
    METHOD 1 : 0(n) time | 0(1) space
"""


def firstNonRepeatingCharacter(string):
    # Write your code here.
    for i, s in enumerate(string):
        if string.count(s) == 1:
            return i
    return -1


""" Question 5 - Longest Palindromic substring. Return the longest palindromic substring.
    e.g: string = 'abaxyzzyxf' -> 'xyzzyx'
    METHOD 1 :  0(n^3) time | 0(n) space
       Two pointers, Two loops, the first loop index is from the start, 
       the second keeps shifting to the right.
       Use a helper function to check if substring is palindrome, 
       if length surpass the last saved result, overrite
    METHOD 2: 0(n^2) time | 0(n) space
        The logic here is to start looping from second index, find the center of both odd and even length, while contineously expanding
        Keep record of the largest index difference from the left to right (Two pointers pulls apart)
"""


def longestPalindromicSubstring(string):
    # 0(n^3) time | 0(n) space

    def is_palindrome(s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # -----
    res = string[0]  # initialize

    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j+1]
            if is_palindrome(substring) and len(substring) > len(res):
                res = substring
    return res


def longestPalindromicSubstring(string):
    # 0(n^2) time | 0(n) space

    def getLongestPalindromeFrom(string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break

            left -= 1
            right += 1

        return [left + 1, right]

    # -----
    sliceIndexes = [0, 1]

    for i in range(1, len(string)):
        even = getLongestPalindromeFrom(string, i-1, i)
        odd = getLongestPalindromeFrom(string, i-1, i+1)

        # Return the greater difference
        longest = max(even, odd, key=lambda x: x[1] - x[0])

        # Return the greater difference
        sliceIndexes = max(sliceIndexes, longest, key=lambda x: x[1] - x[0])

    return string[sliceIndexes[0]:sliceIndexes[1]]


""" Question 6 - Group anagrams 
    e.g: words = ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp'] ->
    [['yo', 'oy'], ['act', 'tac', 'cat'], ['flop', 'olfp'], ['foo']]
    
    METHOD 1 : 0(n *wlogw) time, 0(nw) space
        - Re-arrange each string by sort in ascending, some of the set of words will be the same if its an anagram.
         - Use a hashMap to save indices of anagrams
         - Return the words by the saved up indices in the hashmap
"""


def groupAnagrams(words):
    # - 0(n *wlogw) time, 0(nw) space

    def rearrange(word):
        alphabet = list(word)
        alphabet.sort()
        return ''.join(alphabet)

    # -----
    strs = words
    new_strs = list(map(rearrange, strs))

    hashMap = {}

    for i, w in enumerate(new_strs):
        if w in hashMap:
            hashMap[w].append(i)
        else:
            hashMap[w] = [i]

    return [[strs[i] for i in arr] for _, arr in hashMap.items()]


""" Question 7 - Given a string of digits only, Return an array of possible IP addresses. Such that each part of the IP is has no
    trailing 0 and is in the range 0 - 255. 
    e.g: 
    METHOD 1 - 0(time) | 0(1) space  NOTE: Because the size of the input is at most 12, as stated in the question. As it will always occupy 32bits

"""


def validIPAddresses(string):
    """
    """
    #   Helper function
    def isValidPart(substring):
        if int(substring) > 255:
            return False
        # check for leading 0's
        return len(substring) == len(str(int(substring)))

    # -----
    validIps = []
    for i in range(1, len(string)-2):

        for j in range(i+1, len(string)-1):

            for k in range(j+1, len(string)):

                one = string[0:i]
                two = string[i:j]
                three = string[j:k]
                four = string[k:]

                if isValidPart(one) and isValidPart(two) and isValidPart(three) and isValidPart(four):
                    validIps.append('.'.join([one, two, three, four]))
    return validIps


""" Question 8 - Write a function that takes in a string seperated by one or more whitespaces, and returns a string that has these words
    in reverse order. NOTE: Reverse string must contain the same whitespaces as the original string. DON'T use split() or reverse()
    e.g: AlgoExpert is the best! -> best! the is AlgoExpert
    METHOD 1: 0(n) time | 0(n) space
        - Save all subsequence words & whitespaces in an array, using slow & fast pointers. If whitespace is found, save the preceeding word
          and then accumulate the whitespace until a word starts again
        - Reverse the generated array, using two pointers
    METHOD 2: 0(n) time | 0(n) space
        - Reverse the entire string, 
        - Detect characters before a whitespace is found and reverse the characters within the range.
"""


def reverseWordsInString(string):
    # 0(n) time | 0(n) space

    #   Helper function to reverse
    def reverseList(array):
        left, right = 0, len(array)-1
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # -----
    newString = []

    slow, fast = 0, 1
    while slow < len(string):
        # find the next word
        while fast < len(string) and not string[slow].isspace() and not string[fast].isspace():
            fast += 1
        word = string[slow:fast]
        newString.append(word)

        #   Adjust pointer
        slow = fast
        fast += 1

        # find the next space
        while fast < len(string) and string[slow].isspace() and string[fast].isspace():
            fast += 1
        space = string[slow:fast]
        newString.append(space)

        #   Adjust pointer
        slow = fast
        fast += 1

    # Reverse list
    reverseList(newString)
    return ''.join(newString)
