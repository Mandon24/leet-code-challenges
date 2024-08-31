from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force solution
        # if not nums or len(nums) == 1:
        #     return nums

        # len_nums = len(nums)

        # for i in range(len_nums - 1):
        #     for j in range(len_nums - i - 1):
        #         if nums[j] == 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # Optimized solution
        # return nums
        n1=[]
        n2=[]
        for i in nums:
            if i == 0:
                n2.append(i)
            else:
                n1.append(i)
        nums[:]=n1+n2