class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        row_zero_index = False
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if matrix[row][column] == 0:
                    matrix[0][column] = 0
                    
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero_index = True
                        continue
        
        for row in range(1, ROWS):
            for column in range(1, COLUMNS):
                if matrix[0][column] == 0 or matrix[row][0] == 0:
                    matrix[row][column] = 0
        
        if matrix[0][0] == 0:
            for row in range(ROWS):
                matrix[row][0] = 0
        
        if row_zero_index:
            for column in range(COLUMNS):
                matrix[0][column] = 0