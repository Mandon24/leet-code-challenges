from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            # TODO: use sorted() for strings instead of using lists
            temp_list = list(s)
            temp_list.sort()
            temp_str = ''.join(temp_list)
            
            if temp_str in anagram_map:
                anagram_map[temp_str].append(s)
            else:
                anagram_map.update({temp_str: [s]})

        return [val for val in anagram_map.values()]
