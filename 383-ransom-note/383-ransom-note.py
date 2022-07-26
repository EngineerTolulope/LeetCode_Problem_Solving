class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        if len(magazine) < len(ransomNote):
            return False
        
        ransomSet, magazineSet = {}, {}
        for char in ransomNote:
            if not char in magazine:
                return False
            ransomSet[char] = 1 + ransomSet.get(char, 0)
            
        for char in magazine:
            magazineSet[char] = 1 + magazineSet.get(char, 0)
            
        for char in ransomSet:
            magazine_count = magazineSet.get(char, 0)
            if not ransomSet[char] <= magazine_count:
                return False
        
        return True
            