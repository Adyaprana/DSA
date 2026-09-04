class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])

        zero_rows = []
        zero_columns = []

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    zero_rows.append(row)
                    zero_columns.append(column)

        for r in zero_rows:
            for c in range(columns):
                matrix[r][c] = 0
        
        for c in zero_columns:
            for r in range(rows):
                matrix[r][c] = 0