class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        current_sum = sum(cardPoints[-k:])
        result = current_sum

        for right in range(-k, 0, 1):
            current_sum += (-cardPoints[right] + cardPoints[left])
            result = max(result, current_sum)
            left += 1
        return result

