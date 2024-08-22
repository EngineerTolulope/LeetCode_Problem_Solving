class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous_row = [1]

        print(previous_row)
        for row_num in range(1, rowIndex + 1):
            
            next_row = [0] * (row_num + 1)
            next_row[0], next_row[-1] = 1, 1

            for j in range(len(previous_row)):
                if j + 1 < len(previous_row):
                    next_row[j + 1] += previous_row[j] + previous_row[j + 1]
            previous_row = next_row
            print(previous_row)
        return previous_row

