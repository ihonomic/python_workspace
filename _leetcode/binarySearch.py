def search(nums: list, target: int) -> bool:
    """ Return True, if a target is present in an array thats slightly rotated. 
    - Binary Search 
    """

    if len(nums) == 1:
        if nums[0] != target:
            return False
        else:
            return True

    left, right = 0, len(nums)-1

    while left <= right:

        # remove duplicates
        while left < right and nums[left] == nums[left+1]:
            left += 1
        while left < right and nums[right] == nums[right-1]:
            right -= 1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        #   check to know where to shift the pointers
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


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
