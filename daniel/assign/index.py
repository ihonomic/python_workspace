import os

# 1. GET ALL TXT files in current folder and subfolders
path = "C:/Users/onose/Desktop/scratchpad/daniel/assign/"  # <--  change this to  your current folder

# we shall store all the file names in this list
text_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        # if file is a TXT file, append it to the file list
        if file.endswith("txt"):
            text_files.append(os.path.join(root, file))

values_found = []

# 2.  Loop through all the found txt files
for file in text_files:
    data = open(file, "r").readlines()
    # 3. Loop through the data from current file and find MF value
    for each_line in data:
        # 4. If MF is found, append its value to the list & strip off any spaces
        if each_line.startswith("MF:"):
            values_found.append(each_line[3:].strip())

# 5.  print the results found
print(values_found)
