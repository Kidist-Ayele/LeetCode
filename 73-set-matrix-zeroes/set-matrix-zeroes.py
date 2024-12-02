class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        x, y = [], []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    x.append(row)
                    y.append(col)
        for row in range(rows):
            for col in range(cols):
                if row in x or col in y:
                    matrix[row][col] = 0
                

        