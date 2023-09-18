class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid2), len(grid2[0])
        visited = set()

        def depth_first_search(row, column):
            if row not in range(ROWS) or column not in range(COLUMNS) or (row, column) in visited or grid2[row][column] == 0:
                return True
            
            visited.add((row, column))
            result = grid1[row][column] == 1
            result &= depth_first_search(row - 1, column)
            result &= depth_first_search(row + 1, column)
            result &= depth_first_search(row, column - 1)
            result &= depth_first_search(row, column + 1)
            
            return result
        
        island_count = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid2[row][column] == 1 and (row, column) not in visited and depth_first_search(row, column):
                    island_count += 1
        
        return island_count