class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count_neighbours(row, column):
            neighbour_count = 0
            for r in range(row - 1, row + 2):
                for c in range(column - 1, column + 2):
                    if ((r == row and c == column) or r < 0 or c < 0 or 
                       r == ROWS or c == COLUMNS):
                        continue
                    if board[r][c] in (1, 3):
                        neighbour_count += 1
            return neighbour_count
        
        
        ROWS, COLUMNS = len(board), len(board[0])
        # STATES_MAP = {
        #     0 : (0, 0),  # state: (old, new)
        #     1 : (1, 0),
        #     2 : (0, 1),
        #     3 : (1, 1),
        # }
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                neighbour_count = count_neighbours(row, column)
                
                if board[row][column] and neighbour_count in (2, 3):  # for living cells
                    board[row][column] = 3
                elif not board[row][column] and neighbour_count == 3: # for dead cells
                    board[row][column] = 2
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 1:
                    board[row][column] = 0
                elif board[row][column] in (2, 3):
                    board[row][column] = 1