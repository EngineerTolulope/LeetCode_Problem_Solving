class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        board_length = len(board)

        def get_position_from_square_number(square):
            row = (square - 1) // board_length
            column = (square - 1) % board_length
            if row % 2 != 0:
                column = board_length - 1 - column
            return (row, column)

        visited = set()
        queue = deque([(1, 0)])   # stores (square, number of moves)
        print(queue)
        while queue:
            square, moves_count = queue.popleft()
            for option in range(1, 7):
                new_square = square + option
                new_moves_count = moves_count + 1
                row, column = get_position_from_square_number(new_square)
                if board[row][column] != -1:
                    new_square = board[row][column]
                if new_square == board_length * board_length:
                    return new_moves_count
                if new_square not in visited:
                    visited.add(new_square)
                    queue.append((new_square, new_moves_count))
        return -1

