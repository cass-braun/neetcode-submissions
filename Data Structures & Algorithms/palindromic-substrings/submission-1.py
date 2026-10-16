class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        center = 0

        numPalindrones = 0

        while center < len(s):
            start, end = center, center

            while start > -1 and end <len(s) and s[start] == s[end]:
                numPalindrones += 1
                start-=1
                end+=1

            center += 1

        center, center2 = 0, 1

        while center2 < len(s):
            start, end = center, center2
            
            while start > -1 and end <len(s) and s[start] == s[end]:
                numPalindrones += 1    
                start-=1
                end+=1
                
            center += 1
            center2 += 1

        return numPalindrones
        
        