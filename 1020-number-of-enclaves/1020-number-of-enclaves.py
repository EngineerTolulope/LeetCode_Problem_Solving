class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(row, column):
            if (row < 0 or row == ROWS or column < 0 or column == COLUMNS 
                or (row, column) in visited or not grid[row][column]):
                return 0

            visited.add((row, column))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            result = 1
            for dr, dy in directions:
                result += dfs(row +  dr, column + dy)
            
            return result

        visited = set()
        land, border_land = 0, 0

        for row in range(ROWS):
            for column in range(COLUMNS):
                land += grid[row][column]
                if (grid[row][column] and (row, column) not in visited and 
                    (row in (0, ROWS - 1) or column in (0, COLUMNS - 1))):
                    border_land += dfs(row, column)
        
        return land - border_land