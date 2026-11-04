class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # When a mismatch happens, test the two possible valid slices:
                # 1. Skip left character: s[l+1 ... r]
                # 2. Skip right character: s[l ... r-1]
                sub1 = s[l+1 : r+1]
                sub2 = s[l : r]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            
            l += 1
            r -= 1
            
        return True
