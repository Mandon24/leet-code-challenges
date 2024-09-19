from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest_consec_nums = 0

        list_tracker = []

        for num in nums:
            if not list_tracker:
                list_tracker.append(num)
            else:
                if num == list_tracker[-1] + 1:
                    list_tracker.append(num)
                elif num == list_tracker[-1]:
                    continue
                else:
                    list_tracker.clear()
                    list_tracker.append(num)

            if len(list_tracker) > longest_consec_nums:
                longest_consec_nums = len(list_tracker)

        
        return longest_consec_nums


