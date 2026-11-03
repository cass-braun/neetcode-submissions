class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        outerOs = deque()

        for r in range(ROWS):
            if board[r][0] == 'O':
                outerOs.append([r, 0]) 
                board[r][0] = '#'
            if board[r][COLS-1] == 'O':
                outerOs.append([r, COLS-1])    
                board[r][COLS-1] = '#'
        for c in range(COLS):
            if board[0][c] == 'O' and c != 0 and c != COLS-1:
                outerOs.append([0, c])
                board[0][c] = '#'
            if board[ROWS-1][c] == 'O' and c != 0 and c != COLS-1:
                outerOs.append([ROWS-1, c])
                board[ROWS-1][c] = '#'
        
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while outerOs:
            r, c = outerOs.popleft()

            for dr, dc in d:
                nr, nc = r + dr, c+dc

                if -1 < nr < ROWS and -1 < nc < COLS and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    outerOs.append([nr, nc])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
        

            


            