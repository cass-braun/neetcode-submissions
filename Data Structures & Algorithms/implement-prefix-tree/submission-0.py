class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr:
                curr = curr[c]
            else: 
                return False

        return '*' in curr and curr['*']

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr:
                curr = curr[c]
            else: 
                return False

        return True
        