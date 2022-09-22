class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtracking(remain_string, words):
            if len(remain_string) == 0:
                result.append(' '.join(words))
                return
            
            for word in wordDict:
                if remain_string.startswith(word):
                    words.append(word)
                    backtracking(remain_string[len(word):], words)
                    words.pop()
        
        result = []
        backtracking(s, [])
        return result