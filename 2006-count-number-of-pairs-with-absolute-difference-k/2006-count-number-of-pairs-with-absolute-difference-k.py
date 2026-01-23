class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)

        count = 0
        for x in freq:
            if x + k in freq:
                count += freq[x] * freq[x + k]
        return count