def sqrt(x):
    left, right = 0, x

    def condition(value) -> bool:
        return value * value <= x

    while left < right:
        mid = left + (right - left) // 2

        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid

    return left - 1


# print(sqrt(5))


def binary_serach(value):
    left, right = 0, value

    def condition(mid) -> bool:
        return

    while left < right:
        mid = left + right - left // 2

        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left


nums = [7, 2, 5, 10, 8]
m = 2


def largestSum(nums: list, m: int) -> int:
    """
        Split the array into m subarrays
        - Minimize the sum of the subarrays
    """
    def condition(threshold):
        split_value = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                split_value += 1
                total = num
                if split_value > m:
                    return False

        return True

    left, right = max(nums), sum(nums)

    while left < right:

        mid = left + (right - left) // 2

        if condition(mid):
            right = mid
        else:
            left = mid + 1

        print(left)

    return left


largestSum(nums, m)
