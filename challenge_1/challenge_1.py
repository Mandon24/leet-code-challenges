from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force way
        # for i, val1 in enumerate(nums):

        #     for j, val2 in enumerate(nums):
        #         if j == i:
        #             continue

        #         if (val1 + val2) == target:
        #             return [i, j]
        
        # Optimized solution
        complement_table = {}
        for i, val1 in enumerate(nums):
            complement_table.update({val1: i})

        for j, val2 in enumerate(nums):
            complement_val = target - val2
            
            complement_val_idx = complement_table.get(complement_val, None)
            if not complement_val_idx:
                continue

            if complement_val_idx and complement_val_idx != j:
                return [j, complement_table.get(complement_val)]
