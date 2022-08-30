class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        column_set, positive_diagonal, negative_diagonal = set(), set(), set()
        result = []
        
        def backtracking(row):
            if row == n:
                board_copy = ["".join(r) for r in board]
                result.append(board_copy)
            
            for column in range(n):
                if (column in column_set or 
                    (row + column) in positive_diagonal or (row - column) in negative_diagonal):
                    continue
                
                column_set.add(column)
                positive_diagonal.add(row + column)
                negative_diagonal.add(row - column)
                board[row][column] = 'Q'
                backtracking(row + 1)
                
                column_set.remove(column)
                positive_diagonal.remove(row + column)
                negative_diagonal.remove(row - column)
                board[row][column] = '.'
        backtracking(0)
        return result