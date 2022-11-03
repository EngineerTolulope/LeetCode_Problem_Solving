class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        
        result = 0
        for i in range(len(columnTitle)):
            num = ord(columnTitle[i]) - ord('A') + 1
            result += num * (26 ** i)
        return result