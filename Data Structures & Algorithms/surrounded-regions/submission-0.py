class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        safe = set()

        borders = set()

        for r in range(rows):
            borders.add( (r, 0))
            borders.add((r, cols-1))

        for c in range(cols):
            borders.add((0, c))
            borders.add((rows-1, c))

        def dfs(i, j):
            safe.add((i, j))
            if i+1 < rows and board[i+1][j] == 'O' and (i+1, j) not in safe:
                dfs(i+1, j)

            if i-1 > -1 and board[i-1][j] == 'O' and (i-1, j) not in safe:
                dfs(i-1, j)

            if j+1 < cols and board[i][j+1] == 'O' and (i, j+1) not in safe:
                dfs(i, j+1)  

            if j-1 > -1 and board[i][j-1] == 'O' and (i, j-1) not in safe:
                dfs(i, j-1)  

        for i, j in borders:
            if board[i][j] == 'O':
                dfs(i, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X' 

            