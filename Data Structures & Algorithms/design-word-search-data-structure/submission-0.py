class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:

        def dfs(i, prev_curr):
            curr = prev_curr
            
            for j in range(i, len(word)):
                if word[j] == '.':
                    return any( ( x != '*' and dfs(j+1, curr[x])) for x in curr)


                if word[j] not in curr:
                    return False
                curr = curr[word[j]]
            return '*' in curr

        return dfs(0, self.root)
