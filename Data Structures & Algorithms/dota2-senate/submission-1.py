class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qR = deque()
        qD = deque()
        
        # Populate queues with initial indices of senators
        for i, char in enumerate(senate):
            if char == 'R':
                qR.append(i)
            else:
                qD.append(i)
                
        # Simulate round-based voting
        while qR and qD:
            r_idx = qR.popleft()
            d_idx = qD.popleft()
            
            # The senator with the smaller index bans the other and earns a spot in the next round
            if r_idx < d_idx:
                qR.append(r_idx + n)
            else:
                qD.append(d_idx + n)
                
        return "Radiant" if qR else "Dire"