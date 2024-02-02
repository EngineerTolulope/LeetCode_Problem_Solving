class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        grid_length = len(grid)
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}
        directions = [(0, 1), (1, 0), (1, 1), (1, -1,), 
                      (-1, -1), (-1, 0), (0, -1), (-1, 1)]

        while queue:
            row, column, length = queue.popleft()
            if (min(row, column) < 0 or max(row, column) == grid_length or
                grid[row][column] == 1):
                continue

            if row == grid_length - 1 and column == grid_length - 1:
                return length
            
            for dr, dc in directions:
                new_row, new_column = row + dr, column + dc
                if (new_row, new_column) not in visited:
                    queue.append((new_row, new_column, length + 1))
                    visited.add((new_row, new_column))
        return -1
        