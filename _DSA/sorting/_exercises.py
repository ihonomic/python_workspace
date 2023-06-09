class Solution:

    def __init__(self) -> None:
        pass

    def sortColors_Bubble(self, nums: list) -> None:
        # 1.                                                                                    Bubble Sort
        len_n = len(nums)

        for i in range(len_n):
            for j in range(len_n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    def sortColors_Merge(self, nums: list) -> None:
        # 2.                                                                                    Merge sort
        if len(nums) <= 1:
            return

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        self.sortColors_Merge(left)
        self.sortColors_Merge(right)

        self.merge_two_sorted(left, right, nums)

    def merge_two_sorted(self, a, b, arr):

        len_a = len(a)
        len_b = len(b)

        i = j = k = 0

        while i < len_a and j < len_b:
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1

            k += 1

        #   when one list has been exhuasted
        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1

        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1

        # 3.                                                                                  Quick Sort

    def sortColors_Insertion(self, nums: list) -> None:
        # 4.                                                                                  Insertion Sort
        for i in range(1, len(nums)):
            key = nums[i]

            #   check for condition here. continue if condition are met.
            #   e.g checking if negative,

            #
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j = j - 1

            nums[j+1] = key


if "__main__" == __name__:
    s = Solution()
    arr = [9, 4, 6, 2, 0, 4, 6, 7, 8]
    # s.sortColors_Bubble(arr)
    s.sortColors_Merge(arr)
    # s.sortColors_Insertion(arr)
    print(arr)
