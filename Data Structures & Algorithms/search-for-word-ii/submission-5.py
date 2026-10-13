class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}

        for w in words:
            curr = root
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = w    
        
        rows = len(board)
        cols = len(board[0])
        result_words = set()


        def dfs(r,c, node):
            char = board[r][c]
            
            if char not in node:
                return

            next_node = node[char]

            if '*' in next_node:
                result_words.add(next_node['*'])

            board[r][c] = '#'

            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        
        return list(result_words)
        '''
        def search(i, word, r, c, visited):
            
            down = False
            up = False
            left = False
            right = False

            if i == len(word) -1:
                return True

            if r+1 < rows and [r+1, c] not in visited and board[r+1][c] == word[i+1]:
                newVisited = visited[:]
                newVisited.append([r+1, c])
                down = search(i+1, word, r+1, c, newVisited)

            if r-1 > -1 and [r-1, c] not in visited and board[r-1][c] == word[i+1]:
                newVisited = visited[:]
                newVisited.append([r-1, c])
                up = search(i+1, word, r-1, c, newVisited)

            if c+1 < cols and [r, c+1] not in visited and board[r][c+1] == word[i+1]:
                newVisited = visited[:]
                newVisited.append([r, c+1])
                right = search(i+1, word, r, c+1, newVisited)

            if c-1 > -1 and [r, c-1] not in visited and board[r][c-1] == word[i+1]:
                newVisited = visited[:]
                newVisited.append([r, c-1])
                left = search(i+1, word, r, c-1, newVisited)

            return down or up or right or left

        
        for w in words:
            r = 0
            
            word_found = False
            
            while r < rows and not word_found:
                c = 0
                while c < cols and not word_found:
                    if w[0] == board[r][c]:
                        visited = [ [r, c] ]

                        if search(0, w, r, c, visited):
                            result_words.append(w)
                            word_found = True

                    c+=1
                r +=1
        '''
        return result_words