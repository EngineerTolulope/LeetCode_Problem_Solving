from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length in descending order
        words.sort(key=lambda w: -len(w))
        word_index = {word: i for i, word in enumerate(words)}  # Map word to index
        dp = {}  # Dictionary to store the longest chain length for each word index
        
        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            longest_chain = 1
            current_word = words[i]
            
            for j in range(len(current_word)):
                # Create predecessor by removing one character at each position
                predecessor = current_word[:j] + current_word[j+1:]
                if predecessor in word_index:
                    # Update longest_chain length
                    longest_chain = max(longest_chain, 1 + dfs(word_index[predecessor]))
            
            dp[i] = longest_chain
            return longest_chain
        
        # Apply DFS to each word and find the maximum chain length
        for i in range(len(words)):
            dfs(i)
        
        return max(dp.values(), default=1)

# Example usage:
# solution = Solution()
# print(solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))  # Output: 4
# print(solution.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # Output: 5
# print(solution.longestStrChain(["abcd", "dbqca"]))  # Output: 1
