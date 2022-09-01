class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLUMNS = len(board), len(board[0])
        rows_set = collections.defaultdict(set)
        columns_set = collections.defaultdict(set)
        sub_box_set = collections.defaultdict(set)  	# key is (row//3, column//3)
         
        def backtracking(row, column):
            nonlocal solved
            if row == len(board):
                solved = True
                return
            
            new_row = row + (column + 1) // ROWS
            new_column = (column + 1) % COLUMNS
            if board[row][column] != '.':
                backtracking(new_row, new_column)
            else:
                for num in range(1, 10):
                    if (num not in rows_set[row] and 
                        num not in columns_set[column] and 
                        num not in sub_box_set[(row // 3, column // 3)]):
                        rows_set[row].add(num)
                        columns_set[column].add(num)
                        sub_box_set[(row // 3, column // 3)].add(num)
                        board[row][column] = str(num)
                        
                        backtracking(new_row, new_column)
                        
                        if not solved:
                            rows_set[row].remove(num)
                            columns_set[column].remove(num)
                            sub_box_set[(row // 3, column // 3)].remove(num)
                            board[row][column] = '.'
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                current_value = board[row][column]
                
                if current_value != '.':
                    current_value = int(current_value)
                    rows_set[row].add(current_value)
                    columns_set[column].add(current_value)
                    sub_box_set[(row // 3, column // 3)].add(current_value)
        
        solved = False
        backtracking(0, 0)