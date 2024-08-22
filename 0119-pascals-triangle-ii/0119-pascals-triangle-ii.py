from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the first row of Pascal's Triangle
        current_row = [1]

        # Generate each row up to the rowIndex
        for row_num in range(1, rowIndex + 1):
            # Start each new row with 1
            next_row = [1] * (row_num + 1)

            # Update the internal values of the row based on the previous row
            for j in range(1, row_num):
                next_row[j] = current_row[j - 1] + current_row[j]

            # Move to the next row
            current_row = next_row
        
        return current_row
