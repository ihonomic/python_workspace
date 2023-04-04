#!/usr/bin/python

# Read in the environment variable created by HTML

import os

GET = {}
args = os.getenv("QUERY_STRING").split("&")

for arg in args:
    t = arg.split("=")
    if len(t) > 1:
        kkey = arg.split("=")[0]
        vvalue = arg.split("=")[1]
        GET[kkey] = vvalue

# Get data from fields
first_value = GET["first_value"]
second_value = GET["second_value"]

# Perform tasks using data

sum = str(float(first_value) + float(second_value))

# Return data to print

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>The sum is %s </h2>" % (sum))
print("</body>")
print("</html>")
