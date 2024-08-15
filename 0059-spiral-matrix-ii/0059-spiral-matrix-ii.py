class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        value = 1

        while left <= right and top <= bottom:
            # fill top
            for col in range(left, right + 1):
                matrix[top][col] = value
                value += 1
            top += 1
            # fill right
            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1
            # fill bottom
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = value
                value += 1
            bottom -= 1
            # fill left
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = value
                value += 1
            left += 1
        return matrix

