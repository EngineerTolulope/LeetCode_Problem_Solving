from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = Counter("balloon")
        text_count = Counter(text)

        # Initialize result with maximum possible value
        result = float('inf')

        # Iterate through the characters in 'balloon'
        for char, count in balloon_count.items():
            # Calculate the ratio of occurrence of the character in text to that in 'balloon'
            ratio = text_count[char] // count
            # Update result with the minimum ratio
            result = min(ratio, result)
        
        return result
