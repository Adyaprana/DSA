class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        for row in range(rows):
            for column in range(row+1, columns):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

        for column in range(columns):
            matrix[column].reverse()
        