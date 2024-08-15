class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Initialize the boundaries and the value counter
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        value = 1

        # Continue the loop until the boundaries meet
        while left <= right and top <= bottom:
            # Fill the top row
            for col in range(left, right + 1):
                matrix[top][col] = value
                value += 1
            top += 1
            
            # Fill the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1
            
            # Fill the bottom row (if not already filled)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = value
                    value += 1
                bottom -= 1
            
            # Fill the left column (if not already filled)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = value
                    value += 1
                left += 1
        
        return matrix