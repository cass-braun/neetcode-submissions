class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        cols = {}

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows:
                    matrix[r][c] = 0
                elif c in cols:
                    matrix[r][c] = 0
        
        