class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}

        for word in words:
            curr = root
            for char in word:
                if not char in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['*'] = word
        

        rows = len(board)
        cols = len(board[0])

        d = [(1,0), (-1,0), (0,1), (0,-1)]
        res = []

        def findWord(r, c, curr):
            val = board[r][c]
            

            if val not in curr:
                return
            board[r][c] = '#'
            curr = curr[val]
            
            if '*' in curr and curr['*'] is not None:
                res.append(curr['*'])
                curr['*'] = None
                
            for dr, dc in d:
                nr, nc = r+dr, c+dc

                if 0<=nr<rows and 0 <= nc<cols:
                    findWord(nr, nc, curr)
            
            board[r][c] = val
        
        for r in range(rows):
            for c in range(cols):
                findWord(r, c, root)
        return res
                    
            