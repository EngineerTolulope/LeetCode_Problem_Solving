class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        visited, max_area = set(), 0
        def depth_first_search(row, column):
            if (row < 0 or row == ROWS or column < 0 or column == COLUMNS or
                (row, column) in visited or grid[row][column] == 0):
                return 0
            
            visited.add((row, column))
            area = 1 + (depth_first_search(row - 1, column) +
                        depth_first_search(row + 1, column) +
                        depth_first_search(row, column - 1) +
                        depth_first_search(row, column + 1))
            return area
        
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                area = depth_first_search(row, column)
                max_area = max(max_area, area)
        return max_area
                
            