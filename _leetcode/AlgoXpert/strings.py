"""Question 1 - Caesar Cipher Encryptor
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
    METHOD 1 : 0(n) time | 0(1) space. 
    - Start from second index, 
    - compare with the previous, 
    - count if similar, otherwise, reset count.
                Remember to concatenate the last index from the loop
"""


def runLengthEncoding(string):
    # 0(n) time | 0(1) space
    res = ''
    count = 1
    i = 0

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i - 1]
        if curr == prev and count < 9:
            count += 1
        else:
            res += str(count) + prev
            count = 1
    res += str(count) + string[i]  # NOTE: Handle Last case
    return res


"""Question 3 - Generate documents
    Given a strings of characters and string of document, 
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


"""Question 4 - First Non-repeating character
    Return the index of the first non-repeating character 
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
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # -----
    res = string[0]  # initialize

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
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
        even = getLongestPalindromeFrom(string, i - 1, i)
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)

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


""" Question 7 - Valid Ip address
    Given a string of digits only, Return an array of possible IP addresses. Such that each part of the IP  has no
    trailing 0 and is in the range 0 - 255. 
    e.g: 
    METHOD 1 - 0(n) time  | 0(1) space  NOTE: Because the size of the input is at most 12, as stated in the question.
     As it will always occupy 32bits

"""


def validIPAddresses(string):

    #   Helper function
    def isValidPart(substring):
        if int(substring) > 255:
            return False
        # check for leading 0's
        return len(substring) == len(str(int(substring)))

    # -----
    validIps = []
    for i in range(1, len(string) - 2):

        for j in range(i + 1, len(string) - 1):

            for k in range(j + 1, len(string)):

                one = string[0:i]
                two = string[i:j]
                three = string[j:k]
                four = string[k:]

                if isValidPart(one) and isValidPart(two) and isValidPart(three) and isValidPart(four):
                    validIps.append('.'.join([one, two, three, four]))
    return validIps


""" Question 8 - Reverse words in strings
    Write a function that takes in a string seperated by one or more whitespaces, and returns a string that has these words
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
        left, right = 0, len(array) - 1
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


"""Question 9 - Minimum character of words, 
    Write a func that takes an array of words and returns the smallest array of characters needs to form 
    all the words. They dont need to be in a particular order.
    e.g: words = ["your", "you", "or", "yo"] --> ["y", "r", "o", "u"] 
    METHOD 1:   0(n * c) time, 0(r) space 
        Count the current character in a word and append if it's smaller than that those saved already
"""


def minimumCharactersForWords(words):
    # 0(n * c) time, 0(r) space
    if not words:
        return []

    res = list(words[0])

    for word in words[1:]:
        for char in word:
            # You can also use a counter here.
            if res.count(char) < word.count(char):
                res.append(char)
    return res


""" Question 10 - Longest substring without duplication,
    Write a func that takes in a string and returns the longest substring without duplicate characters
    e.g : string = "clementisacap" --> "mentisac"
    METHOD 1:  0(n) time, 0(1) time
        - Two pointers. 
            Checking each substrings, count its length and compare with previous max if there are no duplicates
"""


def longestSubstringWithoutDuplication(string):
    if len(string) < 2:
        return string

    res = ""
    left = 0
    right = left + 1

    while left < len(string):
        while right < len(string) and string[right] not in string[left:right]:
            res = max([res, string[left:right + 1]], key=len)
            right += 1
        left += 1
    return res


""" Question 11 - Underscorify Substring. Write a func that takes a string and substring, for every substring in string, 
    place an underscore before and after it. 
    Also take note of substrings that sit side by side or overlaps, consider as a single case.
    e.g : string = "testthis is a testtest to see if testestest it works", substring = "test" 
            --> "_test_this is a _testtest_ to see if _testestest_ it works"
    METHOD 1: 0(n) time, 0(n) space
"""


def underscorifySubstring(string, substring):
    # 1. Find the start and end indexes of each cases of the substrings (2D array)
    arrayOfIndexes = []
    for i in range(len(string)):
        start = i
        end = i + len(substring)
        if string[start:end] == substring:
            arrayOfIndexes.append([start, end - 1])

    # print(arrayOfIndexes)
    if not arrayOfIndexes:
        return string

    # 2. Collapse the 2D array to remove overlapping indexes or those sitting side by side
    collapseIndexes = [arrayOfIndexes[0]]
    for i in range(1, len(arrayOfIndexes)):
        lastSaved = collapseIndexes[-1]
        incoming = arrayOfIndexes[i]
        if incoming[0] - lastSaved[1] < 2:
            lastSaved[1] = incoming[1]
        else:
            collapseIndexes.append(arrayOfIndexes[i])

    # print(collapseIndexes)

    # 3. Flatten the 2D list - Take not that start & end idx wil be at even & odd positions respectively
    indexes = []
    for i in collapseIndexes:
        indexes.append(i[0])
        indexes.append(i[1])

    # print(indexes)

    # 3. create new string by inserting underscore before the start and after the end of the 2D indexes
    newString = ""
    for i, s in enumerate(string):
        if i in indexes and indexes.count(i) == 1:
            # Detect if index is at even or odd position
            is_even = indexes.index(i) % 2
            if not is_even:
                newString += '_'
                newString += s
            else:
                newString += s
                newString += '_'

        # Handle cases where there are repeated indexes. [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10,]
        elif i in indexes and indexes.count(i) > 1:
            newString += f'_{s}_'

        else:
            newString += s

    return newString


""" Question 12 - Smallest Substring Containing - Write a func that takes in a big string and small string, 
    return the smallest substring from the big string that contains all characters of the small string. 
    In any order.
    e.g: bigString = "abcd$ef$axb$c$", smallString = "$$abf"
    --> "f$axb$"
    METHOD 1: 0(n * m) time | 0(1) space
        Using two pointers, the slow pointer moving one step at a time, 
        The fast pointer always ahead by smallString length from slow pointer, and
        contineously increasing until the smallString is found. 
        - Compare & update with the last saved
"""


def smallestSubstringContaining(bigString, smallString):
    # Helper function
    def is_validSubstring(slicedPortion, subString):
        for s in subString:
            if slicedPortion.count(s) < subString.count(s):  # can also use Hash table
                return False
        return True

    # ---

    result = ""
    slow = 0

    while slow <= len(bigString) - len(smallString):
        fast = slow + len(smallString)
        while fast < len(bigString):

            slicedPortion = bigString[slow:fast]
            if is_validSubstring(slicedPortion, smallString):
                result = min([result, slicedPortion],
                             key=len) if result else slicedPortion
            fast += 1

        # Last Run.
        slicedPortion = bigString[slow:fast]
        if is_validSubstring(slicedPortion, smallString):
            result = min([result, slicedPortion],
                         key=len) if result else slicedPortion

        slow += 1

    return result


""" Question 13 - Longest Balanced Substring
    e.g: string = "(()))(" --> 4 -- because the longest balanced substring is (())
    METHOD 1: 0(n^3) time, 0(n) space
        - Generate every substring, check if balanced, compare its length with the last saved
    METHOD 2: 0(n) time, 0(n) space
        - Initialize a stack with -1
        - If opening bracket, save its index in a stack, 
        - If closed bracket, pop the last saved index, 
            But If the stack becomes empty as a result of the pop, save the current index of the closed bracket
            Otherwise if after poping there was still an index, substract the current Index
            from the left over index (this is the current length), Now compare with the last saved maximum
    METHOD 3: 0(n) time, 0(1) space
         Count the number of opening and closing brackets. 
        - While looping, If at any time the number of closing exceeds opening, It is not
            balanced. Reset both counts. 
        - But if both counts matches, Record and compare the maximum with the last saved.
        - Lastly, reset counters and Do a reverse Case
"""


# 1.
def longestBalancedSubstring(string):
    # Helper function
    def is_balanced(string):
        stack = []
        for char in string:
            if char == "(":
                stack.append("(")
            elif len(stack) > 0:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        # -->

    maxLength = 0

    for i in range(len(string) + 1):
        for j in range(i + 1, len(string)):
            subString = string[i:j + 1]
            if is_balanced(subString):
                maxLength = max(maxLength, len(subString))

    return maxLength


# 2.
def longestBalancedSubstring(string):
    maxLength = 0
    stack = [-1]

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                currLength = i - stack[-1]
                maxLength = max(maxLength, currLength)

    return maxLength


# 3.
def longestBalancedSubstring(string):
    maxLength = 0
    opening = 0
    closing = 0

    for char in string:
        if char == "(":
            opening += 1
        else:
            closing += 1
            if closing == opening:
                maxLength = max(maxLength, closing + opening)  # OR closing *2
            elif closing > opening:
                opening = 0
                closing = 0

    # Reset counters for reverse Iteration
    opening = 0
    closing = 0

    for char in reversed(string):
        if char == ")":
            closing += 1
        else:
            opening += 1
            if closing == opening:
                maxLength = max(maxLength, closing + opening)
            elif opening > closing:
                opening = 0
                closing = 0
    return maxLength


""" Question 14 - Pattern Matcher 
    Given a pattern of x & y and a string. Return the value of x and y in array, as deduce from the main string
    e.g: pattern = "xxyxxy" string = "gogopowerrangergogopowerranger" -> ["go", "powerranger"]
    
    METHOD 1: 0(n^2 + m ) time | 0(n + m) space 
    - First, Make sure that the given pattern starts with 'x', 
        if not, swap all instances of 'y' to 'x' and all 'x' to 'y' and take note if this swapping happened (flag)
    - Get the counts of 'x' and 'y', take note of the index of the first 'y' (firstYPosition)
    - Determine the length of x & y, 
        Calculate the first y position by determining the length of y
        Generate substring of x starting at first Index, xidx = 1
            we can find length of y =  (len(string) - 1*total x) / total y
            first y poisition yidx = firstYPosition  * len(xSubstring)
"""


def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    #
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]

    # count x & y
    counts = {"x": 0, "y": 0}
    firstYPosition = getFirstYpositionAndCountFrequency(newPattern, counts)

    if counts["y"] != 0:
        # Generating length of x & y
        for lenOfX in range(1, len(string)):
            # A single length of y
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
            if lenOfY <= 0 or lenOfY % 1 != 0:  # NOTE: length can't be 0 or decimal
                continue

            lenOfY = int(lenOfY)  # we know len of single y

            yIdx = firstYPosition * lenOfX
            x = string[:lenOfX]
            y = string[yIdx: yIdx + lenOfY]

            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)

            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        # If no y, generate length of a single x
        lenOfX = len(string) / counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]

    return []


def getNewPattern(pattern):
    patternLetters = list(pattern)
    if patternLetters[0] == "y":
        return list(map(lambda elem: "y" if elem == "x" else "x", patternLetters))
    return patternLetters


""" Question 15 - Palindromic Check
"""


if __name__ == "__main__":
    print(longestSubstringWithoutDuplication("clementisacap"))
    ...
