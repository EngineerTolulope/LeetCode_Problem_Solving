class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, max_heap = '', []
        letters = [('a', a), ('b', b), ('c', c)]
        for char, count in letters:
            if count != 0:
                heapq.heappush(max_heap, (-count, char))
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                result += char2
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, char2))
            else:
                result += char
                count += 1
            if count:
                heapq.heappush(max_heap, (count, char))
        return result
                