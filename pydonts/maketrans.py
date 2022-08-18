from string import ascii_uppercase
s = "#001011010101001"

result = s.translate(
    # str.maketrans({"0": "9", "1": "8"}) OR
    # str.maketrans("01", "98")
    str.maketrans("01", "98", '#')  # Third argument, elements will be removed
)


ABC = ascii_uppercase


def caesar(msg, key):
    return msg.translate(
        str.maketrans(ABC, ABC[key:] + ABC[:key])
    )


print(caesar("HELLO, WORLD", 7))

print('ABCDE'[:15] + "ABCDE"[15:])
