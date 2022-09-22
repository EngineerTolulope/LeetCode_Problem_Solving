class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day():
            new_cells = [0] * 8
            for i in range(1, len(new_cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    new_cells[i] = 1
            return new_cells
        
        found_states = {}
        for i in range(n):
            cells_string = str(cells)
            if cells_string in found_states:
                length_loop = i - found_states[cells_string]
                return self.prisonAfterNDays(cells, (n - i) % length_loop)
            else:
                found_states[cells_string] = i
                cells = next_day()
        return cells