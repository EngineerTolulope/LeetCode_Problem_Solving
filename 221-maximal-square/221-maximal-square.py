class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        max_length = {} # stores the max square length
        def depth_first_search(row, column):
            if row == ROWS or column == COLUMNS:
                return 0
            if (row, column) not in max_length:
                right = depth_first_search(row, column + 1)
                down = depth_first_search(row + 1, column)
                diagonal = depth_first_search(row + 1, column + 1)
                
                max_length[(row, column)] = 0
                if matrix[row][column] == '1':
                    max_length[(row, column)] = 1 + min(right, down, diagonal)
            return max_length[(row, column)]
        
        depth_first_search(0, 0)
        return max(max_length.values()) ** 2