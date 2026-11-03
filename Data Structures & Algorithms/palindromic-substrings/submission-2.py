class Solution:
    def countSubstrings(self, s: str) -> int:
        numSubstrings = 0

        c = 0

        while -1 < c < len(s):
            l, r = c, c
            while -1 < l < len(s) and -1 < r < len(s) and s[l] == s[r]:
                numSubstrings += 1
                l -= 1
                r += 1

            c += 1
        
        c = 0
        while -1 < c < len(s):
            l, r = c, c+1
            while -1 < l < len(s) and -1 < r < len(s) and s[l] == s[r]:
                numSubstrings += 1
                l -= 1
                r += 1

            c += 1

        return numSubstrings
        
        