import os


def load_BE_data_files(dir_name):
    # 1. Move into current directory
    os.chdir(dir_name)

    # 2. Get current directory
    current_dir = os.getcwd()

    # 3. List all files and folders inthe current directory
    all_contents = os.listdir()

    # 4. Ensure you retrieve ONLY folders
    folders = list(filter(lambda x: x.isnumeric(), all_contents))

    # 5. Convert the folder names to intergers and get the maximum, then check if it equals the number of folders
    folders_nums = list(map(int, folders))
    largest_folder = max(folders_nums)
    # largest_folder == len(folders)

    # 6. Sort the folder in ascending order
    folders.sort()

    digitized_files = []
    for digit in folders:
        path = current_dir + "\\" + digit
        for path, dirs, files in os.walk(path):
            for file in files:
                if file.endswith("data"):
                    digitized_files.append(os.path.join(path, file))

    return digitized_files


def get_list_of_all_values(digitized_files, identifier):
    all_values = []
    for file in digitized_files:
        data_ = open(file, "r").readlines()
        for each_line in data_:
            if each_line.startswith(identifier):
                all_values.append(each_line.split(":")[1].strip())

    return all_values


def search_files(digitized_files, key):
    """
    We search for the keyword, if found, we return the entire file content
    otherwise we return None
    """

    for file in digitized_files:
        data_ = open(file, "r").readlines()
        for each_line in data_:
            if key in each_line:
                return data_

    return None


digitized_files = load_BE_data_files(os.getcwd())
values = get_list_of_all_values(digitized_files, "MF")
print("[values found:]", values)

found = search_files(digitized_files, "CF4")
print("[search found:]", found)
