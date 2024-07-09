class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums1, nums2))
        pairs.sort(key = lambda x: x[1], reverse=True)

        result, currentSum, minHeap = 0, 0, []
        for n1, n2 in pairs:
            currentSum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                currentSum -= n1Pop
            if len(minHeap) == k:
                result = max(result, currentSum * n2)
        
        return result


