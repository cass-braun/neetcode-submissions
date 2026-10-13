class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls = len(s)
        lt = len(t)
        
        if lt > ls:
            return ''
        
        count = {}

        for c in t:
            if not c in count:
                count[c] = 0
            count[c] += 1

        required = len(count)
        l,r = 0, 0
        formed = 0
        window = {}

        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) +1

            if char in count and window[char] == count[char]:
                formed +=1

            while l <= r and formed == required:
                nc = s[l]

                if (r - l + 1) <ans[0]:
                    ans = (r - l + 1, l, r)

                window[nc] -= 1

                if nc in count and window[nc] < count[nc]:
                    formed -= 1
                l +=1
            r+=1
        return '' if ans[0] == float('inf') else s[ans[1] : ans[2] +1]
