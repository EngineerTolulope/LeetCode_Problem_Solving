class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def dfs(row, column):
            if (row not in range(ROWS)) or (column not in range(COLUMNS)):
                return 0

            if grid[row][column] == 1 or (row, column) in visited:
                return 1
            
            visited.add((row, column))
            result = 1
            for dr, dc in directions:
                if not dfs(row + dr, column + dc):
                    result = 0
            return result

        result = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] == 0 and (row, column) not in visited:
                    result += dfs(row, column)
        return result