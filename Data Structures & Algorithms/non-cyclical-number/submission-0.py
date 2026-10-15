class Solution:
    def isHappy(self, n: int) -> bool:
        nstr = str(n)

        seen = []
        total = 0
        while total != 1:
            total =0
            for d in nstr:
                d = int(d)
                total += d**2
            if total in seen:
                return False
            print(total)
            seen.append(total)
            nstr = str(total)
        
        return True

