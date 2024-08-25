class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        s_list = [c for c in s]

        order_list = []
        pos_list = []

        for pos, letter in enumerate(s):
            if letter.lower() in vowel_list:
                order_list.append(letter)
                pos_list.append(pos)
        order_list.reverse()

        for new_pos, pos in enumerate(pos_list):
            s_list[pos] = order_list[new_pos]

        return "".join(s_list)
