class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}

        squares = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                
                if val != '.':
                    if r not in rows:
                        rows[r] = []
                    if val in rows[r]:
                        return False
                    
                    rows[r].append(val)

                    if c not in cols:
                        cols[c] = []
                    if val in cols[c]:
                        return False
                    
                    cols[c].append(val)


                    x, y = r// 3, c //3

                    if (x, y) not in squares:
                        squares[(x,y)] = []

                    if val in squares[(x,y)]:
                        return False
                    
                    squares[(x,y)].append(val)
    
        return True