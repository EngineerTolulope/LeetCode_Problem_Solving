class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for i in range(min(len(word1), len(word2))):
            result.append(word1[i])
            result.append(word2[i])
        result.append(word1[i + 1:])
        result.append(word2[i + 1:])
        return "".join(result)
