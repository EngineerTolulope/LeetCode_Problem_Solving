class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, column):
            if (row < 0 or column < 0 or row == ROWS or column == COLUMNS
               or grid[row][column] == 0):
                return 1
            if (row, column) in visited:
                return 0
            
            visited.add((row, column))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            result = 0
            for dx, dy in directions:
                new_row = row + dx
                new_column = column + dy
                result += dfs(new_row, new_column)
            return result
        
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column]:
                    return dfs(row, column)