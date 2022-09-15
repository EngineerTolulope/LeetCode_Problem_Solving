class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = 1 + char_count.get(char, 0)
    
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        del char_count
        
        result = ''
        previous = None
        while max_heap or previous:
            if previous and not max_heap:
                return ''
            
            count, char = heapq.heappop(max_heap)
            result += char
            count += 1
            
            if previous:
                heapq.heappush(max_heap, previous)
                previous = None
            if count != 0:
                previous = (count, char)
        return result
        
    
        