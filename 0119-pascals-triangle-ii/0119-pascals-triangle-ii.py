from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Start with the first row of Pascal's Triangle
        current_row = [1]

        # Build each row of Pascal's Triangle up to the specified rowIndex
        for row_number in range(1, rowIndex + 1):
            # Initialize the next row with 1's at both ends
            next_row = [1] * (row_number + 1)

            # Calculate the values in between the first and last elements
            for i in range(1, row_number):
                next_row[i] = current_row[i - 1] + current_row[i]

            # Move to the next row
            current_row = next_row
        
        return current_row
