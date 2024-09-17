class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution1 - 1306 ms, 16.68 MB
        if not s:
            return 0

        res = []
        longest_substr = 0

        idx = 0
        reset_idx = 1
        while True:
            if idx == len(s):
                break

            if s[idx] in res:
                res.clear()
                idx = reset_idx
                reset_idx += 1

            res.append(s[idx])

            if len(res) > longest_substr:
                longest_substr = len(res)
            idx += 1
        
        return longest_substr
    
        # Solution 2 - 147 ms, 16.8 MB
        # if not s:
        #     return 0

        # start = 0
        # end = 0
        # longest_substr = 0

        # while True:
        #     substr = s[start:end]

        #     if end > len(s):
        #         break
        #     if len(substr) == len(set(substr)):

        #         if longest_substr == 0:
        #             longest_substr = 1 if len(substr) == 0 else len(substr)
        #         elif len(substr) > longest_substr:
        #             longest_substr = len(substr)
        #     else:
        #          start += 1
        #     end += 1
        # return longest_substr

        # Solution 3 - Optmized Solution - 56 ms, 16.72 MB
        # seen = {}
        # l = 0
        # length = 0
        # for r in range(len(s)):
        #     char = s[r]
        #     if char in seen and seen[char] >= l:
        #         l = seen[char] + 1
        #     else:
        #         length = max(length, r - l + 1)
        #     seen[char] = r

        # return length
