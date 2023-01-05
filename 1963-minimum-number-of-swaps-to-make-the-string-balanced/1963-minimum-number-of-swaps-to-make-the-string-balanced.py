class Solution:
    def minSwaps(self, s: str) -> int:
        close, max_close = 0, 0
        
        for bracket in s:
            if bracket == '[':
                close -= 1
            elif bracket == ']':
                close += 1
                max_close = max(close, max_close)
        return (max_close + 1) // 2
            