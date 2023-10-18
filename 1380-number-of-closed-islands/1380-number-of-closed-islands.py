class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(row, column):
            if not (0 <= row < ROWS and 0 <= column < COLUMNS):
                return 0

            if grid[row][column] == 1 or (row, column) in visited:
                return 1

            visited.add((row, column))
            return_result = 1
            for dr, dc in directions:
                return_result &= dfs(row + dr, column + dc)

            return return_result

        final_result = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] == 0 and (row, column) not in visited:
                    final_result += dfs(row, column)

        return final_result