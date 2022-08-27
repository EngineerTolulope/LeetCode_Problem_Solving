class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if matrix[middle_row][-1] < target:
                top = middle_row + 1
            elif matrix[middle_row][0] > target:
                bottom = middle_row - 1
            else:
                break
        
        if top > bottom: # we went out of bounds
            return False
        
        left, right = 0, COLUMNS - 1
        while left <= right:
            middle_index = (left + right) // 2
            middle_num = matrix[middle_row][middle_index]
            
            if middle_num < target:
                left = middle_index + 1
            elif middle_num > target:
                right = middle_index - 1
            else:
                return True
        return False
            