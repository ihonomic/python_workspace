def mod():
    count_less_than_120 = 0
    deepest_tank = 0
    file_path = input("Enter the file name: ")
    try:
        file_content = open(str(file_path), 'r').readlines()

        for percentage_oxygen in file_content:

            maximum_depth = (1.4 / float(percentage_oxygen) - 1) * 33

            print(f"Maximum operating depth is {round(maximum_depth, 1)} feet")

            if maximum_depth < 120:
                count_less_than_120 += 1

            deepest_tank = max(deepest_tank, maximum_depth)

        print(
            f"The number of maximum operating depths less than 120 feet is {count_less_than_120} feet")
        print(
            f"The deepest of the maximum operating depths is {round(deepest_tank, 1)} feet")
        return round(maximum_depth, 1)
    except FileExistsError:
        print("The entered filename can not be found")
        return


mod()

# print(mod(0.32))

# def mod(percentage_oxygen: float) -> float:
#     maximum_depth = (1.4 / percentage_oxygen - 1) * 33
#     return round(maximum_depth, 1)
