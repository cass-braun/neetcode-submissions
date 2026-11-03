class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        pq = []
        maxVal = -float('inf')
        totalVal = len(s)

        for key, value in freq.items():
            heapq.heappush(pq, (-value, key))
            maxVal = max(maxVal, value)
        
        if maxVal > (len(s)+ 1)//2:
            return ''
        
        ans = ''
        wait = None
        while pq:
            freq, letter = heapq.heappop(pq)
            freq *= -1
            freq -= 1
            ans += letter
            if wait is not None:
                heapq.heappush(pq, wait)

            if freq > 0:
                wait = (-freq, letter)
            else:
                wait = None
        return ans