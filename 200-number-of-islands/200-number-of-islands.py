class Solution:
    def depth_first_search(self, grid, row, column):
        grid[row][column] = "0"
        
        # Left, Right, Top, Bottom Neighbors
        neighbors_idx =  [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
        
        for new_row, new_column in neighbors_idx:
            # If the new index is in range and there is an island there, call the method again
            if new_row >= 0 and new_row < len(grid) \
            and new_column >= 0 and new_column < len(grid[new_row]) \
            and grid[new_row][new_column] == "1":
                self.depth_first_search(grid, new_row, new_column)
            
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0
        
        for row in range(len(grid)):    # Go through the rows
            for column in range(len(grid[row])):    # Goes through the column
                if grid[row][column] == "1":
                    self.depth_first_search(grid, row, column)
                    islands_count += 1
        
        return islands_count
                    
                    
                