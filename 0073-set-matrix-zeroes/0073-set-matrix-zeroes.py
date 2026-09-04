class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        """
        rows = len(matrix)
        columns = len(matrix[0])

        zero_rows = set()
        zero_columns = set()

        for row in range(rows):
            for column in range(columns):
                if matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_columns.add(column)

        for r in zero_rows:
            for c in range(columns):
                matrix[r][c] = 0
        
        for c in zero_columns:
            for r in range(rows):
                matrix[r][c] = 0