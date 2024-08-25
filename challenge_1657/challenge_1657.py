class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        # check if same chars - also ignores swapped
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False
        # check if counts add up
        map1 = {}
        map2 = {}
        for c in set1:
            map1[c] = word1.count(c)
        for c in set2:
            map2[c] = word2.count(c)
        set1 = set2 = {}
        count1 = list(map1.values())
        count2 = list(map2.values())
        count1.sort()
        count2.sort()
        if count1 != count2:
            return False
        # at this point words passed all neg test so should be close
        return True
