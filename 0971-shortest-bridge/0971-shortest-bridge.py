class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        length = len(grid)
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_invalid_row_column(row, column):
            return (not (0 <= row < length and 0 <= column < length) or 
                    (row, column) in visited)
                

        def depth_first_search(row, column):
            if is_invalid_row_column(row, column) or grid[row][column] == 0:
                return
            
            visited.add((row, column))
            for dr, dc in directions:
                depth_first_search(row + dr, column + dc)

        def breath_first_search():
            result = 0
            queue = deque(visited)
            while queue:
                for _ in range(len(queue)):
                    row, column = queue.popleft()
                    for dr, dc in directions:
                        new_row, new_column = row + dr, column + dc
                        if is_invalid_row_column(new_row, new_column):
                            continue
                        if grid[new_row][new_column] == 1:
                            return result
                        queue.append((new_row, new_column))
                        visited.add((new_row, new_column))
                result += 1


        for row in range(length):
            for column in range(length):
                if grid[row][column] == 1:
                    depth_first_search(row, column)
                    return breath_first_search()