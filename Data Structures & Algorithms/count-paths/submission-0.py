class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0]* n for _ in range(m)]

        target = [ m-1, n-1 ]
        paths[m-1][n-1] = 1
        d = [(0, 1), (1, 0)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                numPaths = 0
                if r == m-1 and c == n-1:
                    continue

                for dr, dc in d:
                    nr, nc = r+dr, c+dc
                    if -1 < nr < m and -1 < nc < n:
                        numPaths += paths[nr][nc]
                
                paths[r][c] = numPaths
        print(paths)
        return paths[0][0]

