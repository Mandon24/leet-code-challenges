class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        for c_index, letter in enumerate(word1):
            if c_index == (len(word1) - 1):
                merged_word = merged_word + letter + word2[c_index:]
                return merged_word
            elif c_index == (len(word2) - 1):
                merged_word = merged_word + letter + word2[c_index] + word1[c_index+1:]
                return merged_word
            else:
                merged_word = merged_word + letter + word2[c_index]
        
        return merged_word
