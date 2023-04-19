#!/usr/bin/env python3.8

# Read in the environment variable created by HTML

import os

args_array = os.getenv("QUERY_STRING").split("=")
key = str(args_array[1]).replace("+", " ")


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
    folders.sort(key=int)

    digitized_files = []
    for digit in folders:
        path = current_dir + "/" + digit
        for path, dirs, files in os.walk(path):
            for file in files:
                if file.endswith("data"):
                    digitized_files.append(os.path.join(path, file))

    return digitized_files


def search_files(digitized_files, key):
    """
    We search for the keyword, if found, we return the entire file content
    otherwise we return None
    """
    # Refuse searching for single character
    if len(key) <= 1:
        return [{0: ["Keyword not valid"]}]

    keys_found = []
    for folder_number, file in enumerate(digitized_files, 1):
        data_ = open(file, "r").readlines()
        for each_line in data_:
            if key in each_line:
                keys_found.append({folder_number: data_})
                break

    return keys_found if keys_found else [{0: ["No Results Found"]}]


digitized_files = load_BE_data_files(os.getcwd())

result_found = search_files(digitized_files, key)

# print("[search found:]", result_found)


# Return HTML
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>BE_Data - Output</title>")
print("</head>")
print("<body>")


print("<h2> Search Result: %s </h2>" % (str(key)))
print("<hr/>")

for object in result_found:
    for key, value in object.items():
        print("<h4>For entry %s </h4>" % (str(key)))
        for each_line in value:
            print("<p> %s </p>" % (str(each_line)))

print("</body>")
print("</html>")
