class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        start = 0
        max_freq = 0

        for end in range(len(s)):
            endVal = s[end]
            if endVal not in count:
                count[endVal] = 0
            count[endVal] += 1

            max_freq = max(max_freq, count[endVal])

            while (end-start + 1) - max_freq > k:
                count[s[start]] -=1
                start +=1
            
            res= max(res, end-start+1)
        return res