class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            word_count[word] = 1 + word_count.get(word, 0)
            
        max_heap = [(-count, word) for word, count in word_count.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
        