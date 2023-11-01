class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        length = len(grid)
        queue = deque()
        for row in range(length):
            for column in range(length):
                if grid[row][column] == 1:
                    queue.append((row, column))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = -1
        while queue:
            row, column = queue.popleft()
            result = grid[row][column]
            for dr, dc in directions:
                new_row, new_column = row + dr, column + dc
                if (min(new_row, new_column) >= 0 and 
                    max(new_row, new_column) < length and 
                    grid[new_row][new_column] == 0):
                    queue.append((new_row, new_column))
                    grid[new_row][new_column] = grid[row][column] + 1
        
        return result - 1 if result > 1 else -1