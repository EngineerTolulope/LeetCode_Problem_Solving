class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = collections.defaultdict(lambda: 0)
        s2_count = collections.defaultdict(lambda: 0)
        for i in range(len(s1)):
            s1_char, s2_char = s1[i], s2[i]
            s1_count[s1_char] += 1
            s2_count[s2_char] += 1
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_leaving = s2[left]
            s2_new = s2[right]
            s2_count[s2_new] += 1
            s2_count[s2_leaving] -= 1
            
            if s2_count[s2_leaving] == 0:
                s2_count.pop(s2_leaving)

            if s1_count == s2_count:
                return True
            left += 1
        return False
            
            
            
        