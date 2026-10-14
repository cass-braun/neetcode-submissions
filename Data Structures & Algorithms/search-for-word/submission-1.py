class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def checkExist(i, r, c):
            if board[r][c] != word[i]:
                return False

            if board[r][c] == word[i] and i == len(word)-1:
                return True

            val = board[r][c]
            board[r][c] = '#'
            drc = ( (1, 0), (-1, 0), (0, 1), (0, -1))

            hasWord = False

            for dr, dc in drc:
                if 0 <= r+dr < len(board) and 0 <= c+dc < len(board[0]) and board[r+dr][c+dc] != '#':
                    hasWord = hasWord or checkExist(i+1, r+dr, c+dc)

            board[r][c] = val
            return hasWord
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if checkExist(0, i, j):
                    return True
        
        return False