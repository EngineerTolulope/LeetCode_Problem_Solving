class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
            
        stack = stack[:len(stack) - k]
        result = ''.join(stack)
        return str(int(result)) if result else '0'
        
        
        
        
        
        
        # didn't work
#         min_heap = [(-int(c), i) for i, c in enumerate(num)]
#         heapq.heapify(min_heap)
        
#         while k > 0:
#             heapq.heappop(min_heap)
#             k -= 1
        
#         min_heap.sort(key = lambda x: x[1])
#         result = ''
#         for char, _ in min_heap:
#             result += str(-char)
#         return result
        