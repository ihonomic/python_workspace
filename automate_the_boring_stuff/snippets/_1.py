data = ["today", "is", "friday", "friday", "is", "the", "best",
        "day", "of", "week", "weekend", "doesnot", "have", "the", "friday"]


def no_of_occurence(array, p):
    #   Sort by alphabet
    words = [word for word in sorted(array)]

    words_count = {}

    for word in words:
        if not word in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

    #   Arrang by highest values
    words_by_values = sorted(words_count, key=words_count.get, reverse=True)
    print(words_by_values[0:p])
    return words_by_values[0:p]
    ...


# no_of_occurence(data, 3)
