class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        length = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        min_heap = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        while min_heap:
            max_height, row, column = heapq.heappop(min_heap)
            if (row, column) == (length - 1, length - 1):
                return max_height
            
            for dr, dc in directions:
                next_row, next_column = row + dr, column + dc
                if (next_row < 0 or next_column < 0 or 
                    next_row == length or next_column == length or
                    (next_row, next_column) in visited):
                    continue
                    
                visited.add((next_row, next_column))
                new_max_height = max(max_height, grid[next_row][next_column])
                heapq.heappush(min_heap, (new_max_height, next_row, next_column))
                
            