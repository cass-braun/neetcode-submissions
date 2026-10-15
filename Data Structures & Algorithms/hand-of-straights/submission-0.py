class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        freq = {}

        for h in hand:
            if h not in freq:
                freq[h] = 0

            freq[h] += 1
        
        hand.sort()

        for h in hand:
            while freq[h] > 0:
                for i in range(h, h + groupSize):
                    if freq.get(i, 0) > 0:
                        freq[i] -= 1
                    else:
                        return False

        for f in freq:
            if freq[f] != 0:
                return False
        
        return True
                
                



