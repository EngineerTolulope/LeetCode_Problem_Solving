class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        char_index = {}

        for index, char in enumerate(s):
            if char in char_index:
                result = max(result, index - char_index[char] - 1)
            else:
                char_index[char] = index
                
        return result