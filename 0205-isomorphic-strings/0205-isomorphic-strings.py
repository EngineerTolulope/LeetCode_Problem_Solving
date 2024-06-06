class Solution:
    def isIsomorphic(self, str1: str, str2: str) -> bool:
        mapStr1Str2, mapStr2Str1 = {}, {}

        for char1, char2 in zip(str1, str2):
            if ((char1 in mapStr1Str2 and mapStr1Str2[char1] != char2) or
                (char2 in mapStr2Str1 and mapStr2Str1[char2] != char1)):
                return False

            mapStr1Str2[char1] = char2
            mapStr2Str1[char2] = char1
        return True 
