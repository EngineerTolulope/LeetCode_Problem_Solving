class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the row it might be at 
        for row in range(len(matrix)):
            if matrix[row][0] <= target and matrix[row][-1] >= target:
                check = matrix[row] # Extracts the specific row
                
                left, right = 0, len(check) - 1
                while left <= right:
                    if target == check[left] or target == check[right]:
                        return True

                    if target > check[left]:
                        left += 1
                    if target < check[right]:
                        right -= 1

        return False

