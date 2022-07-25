import re


lib = open('matlib.txt', 'r')
text = lib.read()

regexObject = re.compile(r'''
                   (ADJECTIVE|NOUN|VERB)
                   ''', re.VERBOSE).sub('Lion', text)
print(regexObject)
