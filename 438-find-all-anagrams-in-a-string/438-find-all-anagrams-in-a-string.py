class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)
        if s_length < p_length:
            return []
        
        s_count, p_count = {}, {}
        for i in range(p_length):
            s_char, p_char = s[i], p[i]
            p_count[p_char] = 1 + p_count.get(p_char, 0)
            s_count[s_char] = 1 + s_count.get(s_char, 0)
        
        result = []
        left, right = 0, p_length - 1
        while right != s_length:
            if s_count == p_count:
                result.append(left)
            
            if s[left] in s_count:
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    s_count.pop(s[left])
            left += 1
            right += 1
            
            if right < s_length:
                s_count[s[right]] = 1 + s_count.get(s[right], 0)
        
        return result
            
            