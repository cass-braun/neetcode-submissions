class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for c in s:
            if c not in letters:
                letters[c] = 0
            letters[c]+=1

        for ch in t:
            if ch not in letters:
                return False
            else: 
                letters[ch] -= 1
        

        return all(val  == 0for char, val in letters.items())