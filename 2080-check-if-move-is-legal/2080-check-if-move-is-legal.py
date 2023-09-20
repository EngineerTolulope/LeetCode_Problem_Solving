class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        board[rMove][cMove] = color

        def is_valid_position(row, column):
            return 0 <= row < ROWS and 0 <= column < COLUMNS

        def is_legal_move(row, column, color, direction):
            row += direction[0]
            column += direction[1]
            total_length = 1

            while is_valid_position(row, column):
                total_length += 1
                if board[row][column] == ".":
                    return False
                if board[row][column] == color:
                    return total_length >= 3
                row += direction[0]
                column += direction[1]

            return False

        for direction in directions:
            if is_legal_move(rMove, cMove, color, direction):
                return True

        return False