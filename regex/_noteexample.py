import time
import builtins
from pprint import pprint
import random
import ast
# pprint(dir(__builtins__))
# help(time)
# print(time.__doc__)
# print(time.__spec__)
# print(__import__('random'))
# code = '''x = [1, 2]
# print(x)
#     '''
# tree = ast.parse(code)
# print(ast.dump(tree, indent=2))
# print(list(filter(None, '1230 ')))

import re

phoneNumRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is  765-6789 990-890-8765')
print('Phone number found: ' + str(mo.groups()))

batRegex = re.compile(r'Bat(wo)?man')
mo2 = batRegex.search('The Adventures of Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo){2,}man')
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

digitRegex = re.compile(r'(\d{3}-(\d{2})-\d{4})')
s = '222-12-4566'
mo = digitRegex.findall(s)
print(mo)

mo = re.findall('^(\w{2})(la){2}', 'aselalala')
print(mo)

#   Email check
is_email_regex = re.compile(
    r'^([A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+)\.[A-Za-z]{2,})$')

mo = is_email_regex.search('onosetaleoseghale@gmail.com')
if mo:
    print(f'Email found: {mo.group(0)} \nDomain: {mo.group(2)}')

#   Phone check
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 \d{3} # first 3 digits
 (\s|-|\.) # separator
 \d{4} # last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})? # extension
 )''', re.VERBOSE)


agentNamesRegex = re.compile(r'Agent (\w)(\w*)')
r = agentNamesRegex.sub(
    r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# print(r)

# QUESTION 1
samples = ['42', '1,234', '6,368,745',  '12,34,567', '1234']
commaRegex = re.compile(r'''(
     (,\d{3} | ^\d{1})*  # first
     (,\d{3} | ^\d{0,1})  # middle
     (,\d{3} | ^\d{2})$  # end
    )''', re.VERBOSE)
for i in samples:
    mo = commaRegex.search(i)
    if mo:
        print(mo.group())

print('\n')

# QUESTION 2
samples = ['Satoshi Nakamoto', 'Alice Nakamoto', 'RoboCop Nakamoto', 'Satoshi Nakamoto',
           'satoshi Nakamoto', 'Mr. Nakamoto', 'Nakamoto', 'Satoshi nakamoto', ]
regex = re.compile(r'''(
     ^[A-Z]\w+\s(Nakamoto)$
    )''', re.VERBOSE)
for i in samples:
    mo = regex.search(i)
    if mo:
        print(mo.group())
print('\n')

#   QUESTION 3
samples = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.',
           'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']
regex = re.compile(
    r'(^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$)',  re.IGNORECASE)
for i in samples:
    mo = regex.search(i)
    if mo:
        print(mo.group())
print('\n')
