""" THIS IS A TIC TAC TOE GAME OF 2 PLAYERS """
data = {
    "Top-L": " ", "Top-M": " ", "Top-R": " ",
    "Mid-L": " ", "Mid-M": " ", "Mid-R": " ",
    "Low-L": " ", "Low-M": " ", "Low-R": " ",
}


def printboard(data):
    print(f"{data['Top-L']}  |  {data['Top-M']} | {data['Top-R']} ")
    print("---+----+----")
    print(f"{data['Mid-L']}  |  {data['Mid-M']} | {data['Mid-R']} ")
    print("---+----+----")
    print(f"{data['Low-L']}  |  {data['Low-M']} | {data['Low-R']} ")


player = "X"
for i in range(9):
    activeInput = input(f"Player {player} make a move: ")
    data[activeInput] = player

    if player == "X":
        player = "O"
    else:
        player = "X"

    printboard(data)
