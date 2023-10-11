class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        length = min(len(word1), len(word2))

        for i in range(length):
            result.append(word1[i])
            result.append(word2[i])

        if len(word1) > length:
            result.append(word1[length:])
        else:
            result.append(word2[length:])

        return "".join(result)