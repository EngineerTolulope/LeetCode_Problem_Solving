class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or grid2[r][c] == 0
                or (r, c) in visit
            ):
                return True

            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False

            res = dfs(r - 1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c - 1) and res
            res = dfs(r, c + 1) and res
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1
        return count
        
        
        
        ROWS, COLUMNS = len(grid2), len(grid2[0])
        visited = set()

        def depth_first_search(row, column):
            if (row not in range(ROWS) or column not in range(COLUMNS) 
                or (row, column) in visited or grid2[row][column] == 0):
                return True
            
            visited.add((row, column))
            result = True
            if grid1[row][column] == 0:
                result = False


            result = all({result, depth_first_search(row - 1, column),
                                  depth_first_search(row + 1, column),
                                  depth_first_search(row, column - 1),
                                  depth_first_search(row, column + 1)}) 
            return result
        
        
        island_count = 0
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (grid2[row][column] == 1 and depth_first_search(row, column) and
                    (row, column) not in visited):
                    island_count += 1
        return island_count

