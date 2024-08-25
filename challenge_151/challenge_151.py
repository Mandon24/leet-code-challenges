class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split(" ")
        s_list = [word for word in s_list if word != ""]
        s_list.reverse()
        reversed_str = " ".join(s_list)
        return reversed_str
