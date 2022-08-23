class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_set = collections.defaultdict(set)
        columns_set = collections.defaultdict(set)
        sub_box_set = collections.defaultdict(set)  	# key is (row//3, column//3)
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                current_value = board[row][column]
                if current_value == '.':
                    continue
                if (current_value in rows_set[row] or
                    current_value in columns_set[column] or
                    current_value in sub_box_set[(row // 3, column // 3)]):
                    return False
                rows_set[row].add(current_value)
                columns_set[column].add(current_value)
                sub_box_set[(row // 3, column // 3)].add(current_value)
        return True
                    
                    
        