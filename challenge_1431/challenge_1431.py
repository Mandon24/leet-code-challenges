from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        copied_candies = candies.copy()
        copied_candies.sort()

        highest_candies = copied_candies[-1]
        highest_candy_list = []

        for num_candies in candies:
            total_candies = num_candies + extraCandies
            if total_candies >= highest_candies:
                highest_candy_list.append(True)
            else:
                highest_candy_list.append(False)
        return highest_candy_list
