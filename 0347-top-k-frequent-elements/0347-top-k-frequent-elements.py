class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        for bucket in buckets[::-1]:
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result