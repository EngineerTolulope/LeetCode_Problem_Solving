class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        left = 0
        current_sum = 0
        for right in range(len(arr)):
            current_sum += arr[right]

            while right - left + 1 > k:
                current_sum -= arr[left]
                left += 1

            if right - left + 1 == k:
                result += 1 if current_sum / k >= threshold else 0
            
        return result