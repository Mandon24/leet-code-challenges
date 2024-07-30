from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Return False right away if list does not contain 3 elements
        if len(nums) < 3:
            return False

        # Set i and j values to max int allowed in python as starting values
        i_value = float('inf')
        j_value = float('inf')

        # Loop over the list and update i and j values
        # Return True if i and j values are set and there
        # is a num that is greater than both
        for num in nums:
            if num < i_value:
                i_value = num
            elif num > i_value and num < j_value:
                j_value = num
            elif num > i_value and num > j_value:
                return True

        return False
