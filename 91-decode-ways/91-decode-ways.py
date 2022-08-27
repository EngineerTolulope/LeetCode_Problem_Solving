class Solution:
    def numDecodings(self, s: str) -> int:
        num_of_ways = {len(s) : 1}
        
        def depth_first_search(i):
            if i in num_of_ways:
                return num_of_ways[i]
            if s[i] == '0':
                return 0
            
            result = depth_first_search(i + 1)
            if i + 1 < len(s) and (int(s[i:i + 2]) in range(10, 27)):
                result += depth_first_search(i + 2)
            num_of_ways[i] = result
            return result
        
        return depth_first_search(0)