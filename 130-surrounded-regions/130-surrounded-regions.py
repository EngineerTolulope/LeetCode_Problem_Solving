class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLUMNS = len(board), len(board[0])
        
        def depth_first_search(row, column):
            if (row < 0 or row == ROWS or column < 0 or column == COLUMNS or
               board[row][column] != 'O'):
                return
            
            board[row][column] = 'T'
            depth_first_search(row - 1, column)
            depth_first_search(row + 1, column)
            depth_first_search(row, column - 1)
            depth_first_search(row, column + 1)
        
        
        # capture unsurrounded regions. 'O' -> 'T'
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 'O' and (row in (0, ROWS - 1) 
                                                  or column in (0, COLUMNS - 1)):
                    depth_first_search(row, column)
        
        # capture surrounded regions. 'O' -> 'X'
        # uncapture unsurrounded regions. 'T' -> 'O'
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 'O':
                    board[row][column] = 'X'
                elif board[row][column] == 'T':
                    board[row][column] = 'O'
                