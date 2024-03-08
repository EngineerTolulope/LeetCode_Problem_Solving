class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)

        result = 0
        for i in range(length):
            result += mat[i][i]
            result += mat[i][length - 1 - i]

        middle = length // 2
        return result if length % 2 == 0 else result - mat[middle][middle]