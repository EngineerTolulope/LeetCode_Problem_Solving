class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True, key= lambda w : len(w))
        word_index = {word: i for i, word in enumerate(words)}
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            longest_chain = 1
            current_word = words[i]

            for j in range(len(current_word)):
                predecessor = current_word[:j] + current_word[j+1:]
                if predecessor in word_index:
                    longest_chain = max(longest_chain, 1 + dfs(word_index[predecessor]))
                
            dp[i] = longest_chain
            return longest_chain

        for i in range(len(words)):
            dfs(i)

        return max(dp.values(), default=1)