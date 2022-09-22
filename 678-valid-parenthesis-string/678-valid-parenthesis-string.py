class Solution:
    def checkValidString(self, s: str) -> bool:
        open_mincount, open_maxcount = 0, 0
        for char in s:
            if char == '(':
                open_mincount += 1
                open_maxcount += 1
            elif char == ')':
                open_mincount -= 1
                open_maxcount -= 1
            else:
                open_mincount -= 1
                open_maxcount += 1
            
            if open_maxcount < 0:
                return False
            if open_mincount < 0:
                open_mincount = 0
        return open_mincount == 0