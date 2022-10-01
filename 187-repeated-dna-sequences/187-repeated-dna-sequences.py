class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        
        result, seen = set(), set()
        left = 0
        for right in range(9, len(s)):
            sub_string = s[left:right+1]
            if sub_string in seen:
                result.add(sub_string)
            else:
                seen.add(sub_string)
            left += 1
        return list(result)