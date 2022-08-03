class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        time_step, fresh = 0, 0
        queue = deque()
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                value = grid[row][column]
                if value == 1:
                    fresh += 1
                elif value == 2:
                    queue.append((row, column))
                    
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, column = queue.popleft()
                for dx, dy in directions:
                    new_row, new_column = row + dx, column + dy
                    if (new_row < 0 or new_row >= ROWS or 
                        new_column < 0 or new_column >= COLUMNS or 
                        grid[new_row][new_column] != 1):
                        continue
                    else:
                        grid[new_row][new_column] = 2
                        queue.append((new_row, new_column))
                        fresh -= 1
            time_step += 1

        return time_step if fresh <= 0 else -1
        
        