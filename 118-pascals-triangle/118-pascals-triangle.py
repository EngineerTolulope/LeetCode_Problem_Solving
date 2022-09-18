class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for _ in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            row = []
            for i in range(len(temp) - 1):
                row.append(temp[i] + temp[i + 1])
            result.append(row)
        return result