class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        for char in s_count:
            if s_count[char] != t_count.get(char, 0):
                return False
        
        return True

               
#         return sorted(s) == sorted(t)
        
#         s_list, t_list = list(s), list(t)
        
#         s_list.sort()
#         t_list.sort()
        
#         return s_list == t_list
        
        
        
        