from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        no_occurrences = {}
        for num in arr:
            if str(num) in no_occurrences:
                no_occurrences[str(num)] = no_occurrences[str(num)] + 1
            else:
                no_occurrences.update({str(num): 1})

        key_values = list(no_occurrences.values())
        set_values = set(no_occurrences.values())

        if len(key_values) != len(set_values):
            return False

        return True