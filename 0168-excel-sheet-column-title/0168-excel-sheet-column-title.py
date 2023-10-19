class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            result.append(chr(ord('A') + offset))
            columnNumber //= 26
        return ''.join(result[::-1])

    def convertToTitle_(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            result += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26
        return result[::-1]