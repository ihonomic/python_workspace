#!/usr/bin/python

# Read in the environment variable created by HTML

import os

args_array = os.getenv("QUERY_STRING").split("=")
entry_number = args_array[1]


def load_BE_data_files(dir_name):
    # 1. Move into current directory
    os.chdir(dir_name)

    # 2. Get current directory
    current_dir = os.getcwd()

    # 3. List all files and folders inthe current directory
    all_contents = os.listdir()

    # 4. Ensure you retrieve ONLY folders
    folders = list(filter(lambda x: x.isnumeric(), all_contents))

    # 5. Sort the folder in ascending order
    folders.sort()

    digitized_files = []
    for digit in folders:
        path = current_dir + "\\" + digit
        for path, dirs, files in os.walk(path):
            for file in files:
                if file.endswith("data"):
                    digitized_files.append(os.path.join(path, file))

    return digitized_files


digitized_files = load_BE_data_files(os.getcwd())

file_path = digitized_files[int(entry_number)]

data_ = open(file_path, "r").readlines()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>BE_Data - Output</title>")
print("</head>")
print("<body>")
print("<h2> Search Result for Entry Number: %s </h2>" % (str(entry_number)))
print("<hr/>")
for each_line in data_:
    print("<h4> %s </h4>" % (str(each_line)))
print("</body>")
print("</html>")
