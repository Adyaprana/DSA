class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        result = []
        for i in range(columns):
            result.append([0] * rows)
        for row in range(rows):
            for column in range(columns):
                result[column][row] = matrix[row][column]
        return result