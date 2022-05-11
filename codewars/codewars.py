#  List filtering
# basket = ["apple", "strawberry", "orange", "blueberry", ]

# #  Option 1
# berries = []
# for fruit in basket:
#     if "berry" in fruit:
#         berries.append(fruit)

# # option 2 LIST COMPREHENSION
# berries = [fruit for fruit in basket if "berry" in fruit]


# # Option 3 - filter method - return an object - list(berries)
# def berry(fruit):
#     return "berry" in fruit


# berries = filter(berry, basket)

# # option 4 - filter method with lambda
# berries = filter(lambda fruit: 'berry' in fruit, basket)

# print(list(berries))


#   Codewars chanlledge 1
import math
from os import error


def divisors(integer):
    results = [divisor for divisor in range(
        2, integer) if integer % divisor == 0]

    if len(results) == 0:
        return f"{integer} is prime"
    else:
        return results


# print(divisors(14))

#   Codewars chanlledge 2


def dnaStrand(letters):
    ref = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }
    # print(''.join([ref[letter] for letter in letters]))
    return ''.join([ref[letter] for letter in letters])


dnaStrand("ATGC")

#   Codewars chanledge- Question
"""Your task is to sort a given string. Each word in the string will contain a single number.
 This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will 
only contain valid consecutive numbers."""

""" Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  """""


def order(sentence):
    if sentence == '':
        return ''
    else:
        sentence = sentence.split()
        dic = {}
        result = []
        for word in sentence:
            for letter in word:
                if letter in '123456789':
                    dic[int(letter)] = word
        key = 1
        while key < 10:
            try:
                result.append(dic[key])
            except KeyError:
                print(f"{key} not found in dic")
            key += 1
        return " ".join(result)


# print(order("7same wa6y tell2 t1hink wi5ll would4 s3mall com8e"))


#   Codewars challange
""" QUESTION: Write a function that takes a string and return the rate of errors of characters. where n-z is the error
characters."""


def printer_error(s):
    error = "nopqrstuvwxyz"
    return f"{len([letter for letter in s if letter in error ])}/{len(s)}"


# print(printer_error("abcdefghihabcd"))

#   Automate the boring stuff chanledge
""" QUESTION: Write a function that takes a list value as an argument and returns 
a string with all the items separated by a comma and a space, with "and"
inserted before the last item."""
spam = ['apples', 'bananas', 'tofu', 'cats', 'yam', 'dr', "yam", "bread"]


def make_sentence(spam):
    spam.insert(-1, "and")
    s = ', '.join(spam[:-2])
    n = ' '.join(spam[-2:])
    print(f"{s} {n}")
    return f"{s} {n}"


# make_sentence(spam)

#   Codewars chanledge
""" Extract the domain name of a url """


def domain_name(url):
    if "." in url and url.index(".") == 3:
        slice2 = url[4:]  # if www.sefa.ru/ghhh -> sefa.ru/ghhh
    else:
        try:
            s = url.index("/")
            # else https://www.sefa.ru/ghhh -> www.sefa.ru/ghhh
            slice1 = url[s+2:]
        except ValueError:
            slice1 = url

        if "." in slice1 and slice1.index(".") == 3 and slice1.count(".") != 1:
            slice2 = slice1[4:]  # sefa.ru/ghhh
        else:
            slice2 = slice1

    #   Getting the final slice index for sefa.ru/ghhh
    if "." in slice2:
        index = slice2.index(".")
        # print(slice2[:index])
        return slice2[:index]
    else:
        # print(slice2)
        return "exp"


domain_name("https://123.net")
domain_name("icann.org")
domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")
domain_name("url")

# Codewars challedge
""" QUESTION: Write a function that will convert a string into title case, given an optional list of exceptions (minor words).  
The list of minor words will be given as a string with each word separated by a space. 
Your function should ignore the case of the minor words string except  that the first word Must be title case -- it should behave in the same way even if the case of the minor word string is changed."""


def title_case(title, minor_words=''):
    compose, option = title.lower().capitalize().split(), minor_words.lower().split()
    return " ".join([word.lower() if word in option else word.title()
                     for word in compose])


title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
# ==========Codewars Chanledge _ Count duplicate in a string ======


def duplicate_count(text):
    my_dict = {}
    count = 0
    for letter in text.lower():
        my_dict.setdefault(letter, 0)
        my_dict[letter] += 1
    for k, v in my_dict.items():
        if v > 1:
            count += 1
    return count


duplicate_count("aAaabrzza")
duplicate_count("")
duplicate_count("wertrewszxcvb")

#   ========== Codewars ===========
""" Question: """


def zero(operation=None):  # your code here
    return 0 if operation == None else operation(0)


def one(operation=None):  # your code here
    return 1 if operation == None else operation(1)


def two(operation=None):  # your code here
    return 2 if operation == None else operation(2)


def three(operation=None):  # your code here
    return 3 if operation == None else operation(3)


def four(operation=None):  # your code here
    return 4 if operation == None else operation(4)


def five(operation=None):  # your code here
    return 5 if operation == None else operation(5)


def six(operation=None):  # your code here
    return 6 if operation == None else operation(6)


def seven(operation=None):  # your code here
    return 7 if operation == None else operation(7)


def eight(operation=None):  # your code here
    return 8 if operation == None else operation(8)


def nine(operation=None):  # your code here
    return 9 if operation == None else operation(9)


def plus(x):  # your code here
    return lambda y: y + x


def minus(x):  # your code here
    return lambda y: y - x


def times(x):  # your code here
    return lambda y: y * x


def divided_by(x):  # your code here
    return lambda y: y // x  # (if x!=0 else 0)


# print(eight(minus(three())))  # return 5
# print(six(divided_by(two())))  # return 3
# print(two(plus(five())))  # return 7
# print(five(plus(two())))  # return 7
# print(seven(times(five())))  # return 35
# print(seven(times(five())))  # must return 35

#   Codewars Chanledge
'''
Question: interchange the first word to the end and add 'ay'
'''


def pig_it(text):
    return ' '.join([word[1:] + word[0]+'ay' if len(word) > 1 else word if word in "!?" else word[0]+'ay' for word in text.split(' ')])


pig_it('Pig latin is cool')

print(eight(minus(three())))  # return 5
print(six(divided_by(two())))  # return 3
print(two(plus(five())))  # return 7
print(five(plus(two())))  # return 7
print(seven(times(five())))  # return 35
print(seven(times(five())))  # must return 35


#    Capitalize strings base on index


def capitalize_stringIndex(word):
    letters = []
    for letter in range(len(word)):
        if letter % 2 == 0:
            letters.append(word[letter].upper())
        else:
            letters.append(word[letter].lower())
    return ''.join(letters)


def capitalize_stringIndex(word):
    return ''.join([word[index].upper() if index % 2 == 0 else word[index].lower() for index in range(len(word))])


# print(capitalize_stringIndex("abcdefg"))

#   =========== while loop=
# while True:
#     print("who are you? ")
#     name = input()
#     if name != "ihon":
#         continue
#     print("hello Ihon, What is the password ? ")
#     password = input()
#     if password == '':
#         break
# print("Eligible to be here ")

# ==========================================
# def breakWords(words):
#     num_words = len(words)
#     if num_words % 2 == 0:
#         first = words[0:2]
#         sec = words[2:4]
#     else:
#         first = words[0:2]
#         sec = words[2:4] + "_"

#     array = []
#     array.append(first)
#     array.append(sec)
# for index in range(len(words)):
#     if index % 2 != 0:
#         array.append(words[0:index+1])
#     else:
#         array.append(words[0:index+1] + "_")
#     return array


# print(breakWords("a"))

#   =======================
# import random
# random_number = random.randint(0, 21)
# print(random_number)
# count = 0
# while True:
#     count = count + 1
#     print("I am thinking of a number between 1 and 20.")
#     number = input("Take a guess: ")
#     if int(number) < random_number:
#         print("Your guess is too low.")
#         continue
#     elif int(number) > random_number:
#         print("Your guess is too high.")
#         continue
#     else:
#         print("Great Guess !")
#         break
# print(f"It took you {count} guesses")

#   ======================
"""Question: return the number of times the digits of a given number multiplies it's self until it reaches a single number.  persistence"""


def persistence(num):
    realist = list(str(num))
    count = 0
    while len(realist) > 1:
        count += 1
        realist = list(str(math.prod([int(i) for i in realist])))

    return count


persistence(39)


def roman(word):
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    transfrom = []
    for letter in word:
        # if letter in dic:  # No-Need for this - Question says letter MUST always be a roman numeral
        #   check if the letter key has a value bigger than the last appended
        try:
            if transfrom[-1] and dic[letter] > transfrom[-1]:
                newValue = dic[letter] - transfrom[-1]
                #   remove that value
                transfrom[-1] = 0
                #   add the new value
                transfrom.append(newValue)
            else:
                transfrom.append(dic[letter])
        except:
            transfrom.append(dic[letter])
    return sum(transfrom)


roman("I")
roman("IV")
roman("MMVIII")
roman("MDCLXVI")
roman("XXI")
roman("CM")


def displayInventory(my_dict):
    total_items = 0
    print("My Inventory \n")
    for k, v in my_dict.items():
        total_items += v
        # print(k, v)
    print("Total item cost :", total_items)


# displayInventory(
#     {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    vv = {**inventory}
    for item in addedItems:
        vv.setdefault(item, 0)
        vv[item] = vv[item] + 1

    return vv


result = addToInventory(inv, dragonLoot)
displayInventory(result)


#   Codewars chanlledge
""" Question :: Generate harshtag """


def generate_hashtag(s):
    sentence = s.title()
    word = "".join(list(sentence.replace(" ", "")))
    if not s or len(word) > 140:
        return False
    return "#"+word


generate_hashtag("Codewars Is Nice")

print("==========================================")


def count_change(total, arr):
    count = 0
    if sum(arr) == total:
        count += 1
        #   add each number to it self and until it equals the total
    for num in arr:
        while num < total:
            num += num
            if num == total:
                count += 1
                print(count)
                break
        #   consider a single num , substract from the total
        #   see if the rest nums amount to the result of the substravtion
    for num in arr:
        substract = total - num
        # this is what's left to complete the total

        newArr = [] + arr
        newArr.remove(num)
        if num + sum(newArr) == total:
            count += 1

    print(count)
    return count


# count_change(4, [2, 2])
count_change(4, [1, 2])  # => 3
# count_change(10, [5, 2, 3])  # => 4
# count_change(11, [5, 7])  # => 0
