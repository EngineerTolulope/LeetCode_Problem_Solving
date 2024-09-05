class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        result = [[None for _ in range(ROWS)] for _ in range(COLUMNS)] 
        for row in range(ROWS):
            for column in range(COLUMNS):
                result[column][row] = matrix[row][column]
        
        return result