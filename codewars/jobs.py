def maximum_amount(wealths) -> int:

    total_houses = len(wealths)

    if total_houses == 0:
        return 0
    if total_houses == 1:
        return wealths[0]
    if total_houses == 2:
        return max(wealths[0], wealths[1])

    houses = [0] * total_houses

    # Initialize the houses[0] and houses[1]
    houses[0] = wealths[0]
    houses[1] = max(wealths[0], wealths[1])

    # Fill remaining positions - Fibbonacci
    for i in range(2, total_houses):
        houses[i] = max(wealths[i] + houses[i-2], houses[i-1])

    return houses[-1]


case1 = maximum_amount([2, 10, 14, 8, 1])
case2 = maximum_amount([2, 5, 1, 3, 6, 2, 4])
case3 = maximum_amount([120, 500, 700, 200])

print(case1)
print(case2)
print(case3)
