class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLUMNS = len(grid), len(grid[0])
        result = [[0] * COLUMNS for row in range(ROWS)]
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                new_val = (row * COLUMNS + column + k) % (ROWS * COLUMNS)
                new_r, new_c = new_val // COLUMNS, new_val % COLUMNS
                result[new_r][new_c] = grid[row][column]
        return result
                