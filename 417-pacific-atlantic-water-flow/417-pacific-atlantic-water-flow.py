class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## Helper Function
        def depth_first_search(row, column, visited, previous_height):
            # If position has been visited, or out of bounds, or not a valid height             
            if ((row, column) in visited or
                row < 0 or column < 0 or row == row_len or column == column_len
                or heights[row][column] < previous_height):
                    return
            
            # We get here if the above if condition is not valid
            visited.add((row, column))  # Adds a tuple to the set
            
            neighbors_idx =  [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]
            for r, c in neighbors_idx:  # Calls the dfs function recursively on each neighbor
                depth_first_search(r, c, visited, heights[row][column])                             
        ## End of Function
        
        
        ## Main Function
        row_len, column_len = len(heights), len(heights[0]) # The row and column lengths
        pacific_visited, atlantic_visited = set(), set()    # Hash set to store visited areas
        
        # Performs a depth first search on the top and bottom rows
        for column in range(column_len):
            depth_first_search(0, column, pacific_visited, heights[0][column])
            depth_first_search(row_len - 1, column, atlantic_visited, heights[row_len - 1][column])
            
        # Performs a depth first search on the left and right columns
        for row in range(row_len):
            depth_first_search(row, 0, pacific_visited, heights[row][0])
            depth_first_search(row, column_len - 1, atlantic_visited, heights[row][column_len - 1])
                
        # Checks if there a collision in both sets
        collisions = []
        for row in range(row_len):
            for column in range(column_len):
                if (row, column) in pacific_visited and (row, column) in atlantic_visited:
                    collisions.append([row, column])
                    
        return collisions
        