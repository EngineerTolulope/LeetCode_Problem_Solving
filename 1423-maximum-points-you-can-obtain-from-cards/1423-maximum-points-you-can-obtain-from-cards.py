from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Calculate the sum of the last k elements in the cardPoints
        current_sum = sum(cardPoints[-k:])
        max_score = current_sum  # Initialize the maximum score with the sum of the last k elements

        # Use a sliding window approach to explore all possible combinations
        for left in range(k):
            # Move the window: subtract the cardPoint that is going out and add the one coming in
            current_sum = current_sum - cardPoints[-(k - left)] + cardPoints[left]
            max_score = max(max_score, current_sum)  # Update the maximum score if needed

        return max_score

    def maxScore_(self, cardPoints: List[int], k: int) -> int:
        left = 0
        current_sum = sum(cardPoints[-k:])
        result = current_sum

        for right in range(-k, 0, 1):
            current_sum += (-cardPoints[right] + cardPoints[left])
            result = max(result, current_sum)
            left += 1
        return result

