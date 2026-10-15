class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return matrix

        start = 1
        end = len(matrix)

        c = 0

        while c < len(matrix[0]):
            for r in range(start, end):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
            start+=1
            c+=1
    
        for m in matrix:
            m.reverse()


