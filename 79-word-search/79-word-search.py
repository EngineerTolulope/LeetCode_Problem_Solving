class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        visited = set()
        
        def depth_first_search(row, column, index):
            if index == len(word):
                return True
            if (row < 0 or column < 0 or row == ROWS or column == COLUMNS
               or board[row][column] != word[index] or (row, column) in visited):
                return False
            
            visited.add((row, column))
            result = (depth_first_search(row, column - 1, index + 1) or
                      depth_first_search(row, column + 1, index + 1) or
                      depth_first_search(row - 1, column, index + 1) or
                      depth_first_search(row + 1, column, index + 1))
            visited.remove((row, column))
            return result
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if depth_first_search(row, column, 0):
                    return True
        return False