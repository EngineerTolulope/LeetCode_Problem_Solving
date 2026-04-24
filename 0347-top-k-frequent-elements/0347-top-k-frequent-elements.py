class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(min_heap)
            result.append(num)
        
        return result