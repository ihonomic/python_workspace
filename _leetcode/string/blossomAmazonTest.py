def formatDate(strArr: list) -> list:
    """ Re-format dates in the array  -> ['1972-03-04', ... n] """

    d = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    stack = []

    for date in strArr:
        subArray = date.split()

        day = subArray[0][:-2]

        if len(day) == 1:
            day = "0"+day

        stack.append(
            f'{subArray[2]}-{d[subArray[1]]}-{day}'
        )

    return stack


# -> ['1972-03-14', '1904-04-07', '2014-12-22']
print(formatDate(['14th Mar 1972', '7th Apr 1904', '22nd Dec 2014']))
