class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        infinity = float('infinity')
        result = [[infinity] * (COLUMNS + 1) for _ in range(ROWS + 1)]
        result[ROWS - 1][COLUMNS] = 0
        
        for row in range(ROWS - 1, -1, -1):
            for column in range(COLUMNS - 1, -1, -1):
                result[row][column] = (grid[row][column] 
                                       + min(result[row + 1][column], result[row][column + 1]))
        return result[0][0]