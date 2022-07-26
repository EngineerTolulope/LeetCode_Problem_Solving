class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(mat), len(mat[0])
        queue = []
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = '#'
        
        directions = (0, -1), (0, 1), (-1, 0), (1, 0)   # left, right, up, down
        for row, col in queue:
            for dx, dy in directions:
                nrow = row + dx
                ncol = col + dy
                
                if 0 <= nrow < ROWS and 0 <= ncol < COLUMNS and mat[nrow][ncol] == '#':
                    mat[nrow][ncol] = mat[row][col] + 1
                    queue.append((nrow, ncol))
        return mat
            
                
        