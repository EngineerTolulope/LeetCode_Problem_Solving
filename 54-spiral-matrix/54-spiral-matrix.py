class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, buttom = 0, len(matrix)
        
        while left < right and top < buttom:
            # for every i in top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            
            # for every i in right row
            for i in range(top, buttom):
                result.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < buttom):
                break
            
            # for every i in buttom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[buttom - 1][i])
            buttom -= 1
            
            # for every i in left row
            for i in range(buttom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result    
        
            