#   Without using oython default, sort a list
def sorting(arr: list) -> list:
    if not arr:
        return []
    m = max(arr)
    idx = arr.index(m)
    return [m] + sorting(arr[:idx]+arr[idx+1:])


print(sorting([4, 5, 2, 7, 2, 9, 3]))

# 2. Fibonacci sequence

# 3. Factorial - Without using math.factorial
