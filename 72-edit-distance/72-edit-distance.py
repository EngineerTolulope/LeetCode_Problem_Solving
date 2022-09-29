class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[sys.maxsize] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for row in range(len(word1) + 1):
            dp[row][len(word2)] = len(word1) - row
        for column in range(len(word2) + 1):
            dp[len(word1)][column] = len(word2) - column
        
        for row in range(len(word1) - 1, -1, -1):
            for column in range(len(word2) - 1, -1, -1):
                if word1[row] == word2[column]:
                    dp[row][column] = dp[row + 1][column + 1]
                else:
                    dp[row][column] = 1 + min(dp[row + 1][column + 1],
                                              dp[row + 1][column],
                                              dp[row][column + 1])
        return dp[0][0]
                