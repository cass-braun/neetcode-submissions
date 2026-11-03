from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if '0000' in deadends_set:
            return -1
        

        q = deque([ ('0000', 0)]) #(value, numTurns)
        visited = {'0000'}
        while q:
            value, numTurns = q.popleft()

            if value == target:
                return numTurns
            
            vArr = list(value)

            for i in range(4):
                e = vArr[i]
                e = int(e)

                upE = (e+1)%10

                downE = (e-1)%10

                upStr = ''.join(vArr[:i] + [str(upE)] + vArr[i+1:])
                downStr = ''.join(vArr[:i] + [str(downE)] + vArr[i+1:])

                if upStr not in deadends_set and upStr not in visited:
                    visited.add(upStr)
                    q.append((upStr, numTurns+1))
                if downStr not in deadends_set and downStr not in visited:
                    visited.add(downStr)
                    q.append((downStr, numTurns+1))

                vArr[i] = str(e)

        return -1
