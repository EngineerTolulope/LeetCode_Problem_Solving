class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        maximum_path = {} # dynamic programming
        
        def depth_first_search(row, column, previous_value):
            if (row not in range(0, ROWS) or column not in range(0, COLUMNS)
               or matrix[row][column] <= previous_value):
                return 0
            if (row, column) in maximum_path:
                return maximum_path[(row, column)]
            
            result = max(1, 1 + depth_first_search(row - 1, column, matrix[row][column]),
                        1 + depth_first_search(row + 1, column, matrix[row][column]),
                        1 + depth_first_search(row, column - 1, matrix[row][column]),
                        1 + depth_first_search(row, column + 1, matrix[row][column]))
            maximum_path[(row, column)] = result
            return result
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                depth_first_search(row, column, -1)
                
        return max(maximum_path.values())
        
        