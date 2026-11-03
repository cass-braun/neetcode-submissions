class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0: heapq.heappush(pq, (-a, 'a'))
        if b > 0: heapq.heappush(pq, (-b, 'b'))
        if c > 0: heapq.heappush(pq, (-c, 'c'))
        
        ans = []
        
        while pq:
            freq1, char1 = heapq.heappop(pq)
            
            # Check if the last two characters in our answer are the same as char1
            if len(ans) >= 2 and ans[-1] == char1 and ans[-2] == char1:
                # If we can't use char1, we must use the second-best character
                if not pq:
                    break # No other characters available to break the streak
                
                freq2, char2 = heapq.heappop(pq)
                ans.append(char2)
                
                # Put char2 back if it still has remaining count
                if freq2 + 1 < 0:
                    heapq.heappush(pq, (freq2 + 1, char2))
                    
                # Put char1 back into the heap for the next turn
                heapq.heappush(pq, (freq1, char1))
            else:
                # Safe to use char1 (use up to 2 times if available)
                ans.append(char1)
                if freq1 + 1 < 0:
                    heapq.heappush(pq, (freq1 + 1, char1))
                    
        return "".join(ans)