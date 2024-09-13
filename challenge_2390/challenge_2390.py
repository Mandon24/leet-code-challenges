from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        # my solution (ugly solution)
        if not s:
            return ""
        
        star_stack = deque()
        letter_stack = deque()
        temp_stack = deque()

        for i, c in enumerate(s):
            if c == "*":
                star_stack.append(i)
            else:
                letter_stack.append(i)
        

        while star_stack:
            if not letter_stack:
                break

            star_idx = star_stack.pop()
            letter_idx = letter_stack.pop()

            while star_idx < letter_idx:
                temp_stack.append(letter_idx)
                letter_idx = letter_stack.pop()

                
        while letter_stack:
            temp_stack.append(letter_stack.pop())

        final_str = ""
        while temp_stack:
            final_str += s[temp_stack.pop()]
        
        return final_str

    # simple solution (using stack)
    # class Solution:
    # def removeStars(self, s: str) -> str:
    #     stack = []
    #     for char in s:
    #         if char.isalpha():
    #             stack.append(char)
    #         elif stack:
    #             stack.pop()
    #     return "".join(stack)

    # simple solution (using string operations)
    # class Solution:
    # def removeStars(self, s: str) -> str:
    #     res = ""
    #     i = 0
    #     while i < len(s):
    #         if s[i] == '*':
    #             res = res[:-1]  # Remove the last character from res
    #             i += 1 
    #         else:
    #             res += s[i]
    #             i += 1
    #     return res