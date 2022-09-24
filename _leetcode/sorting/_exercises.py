class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.                                                                                    Bubble Sort
        # len_n = len(nums)
        # for i in range(len_n):
        #     for j in range(len_n-1-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1] , nums[j]

        # 2.                                                                                    Merge sort
    #     if len(nums) <= 1:
    #         return

    #     mid = len(nums) // 2

    #     left = nums[:mid]
    #     right = nums[mid:]

    #     self.sortColors(left)
    #     self.sortColors(right)

    #     self.merge_two_sorted(left, right, nums)

    # def merge_two_sorted(self, a, b, arr):

    #     len_a = len(a)
    #     len_b = len(b)

    #     i = j = k = 0

    #     while i < len_a and j < len_b:
    #         if a[i] <= b[j]:
    #             arr[k] = a[i]
    #             i += 1
    #         else:
    #             arr[k] = b[j]
    #             j += 1

    #         k += 1

    #     #   when one list has been exhuasted
    #     while i < len_a:
    #         arr[k] = a[i]
    #         i += 1
    #         k += 1

    #     while j < len_b:
    #         arr[k] = b[j]
    #         j += 1
    #         k += 1

        # 3.                                                                                  Quick Sort
