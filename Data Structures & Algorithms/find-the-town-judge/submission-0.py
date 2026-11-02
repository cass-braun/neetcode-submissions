class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [ [] for _ in range(n) ] #index = trusted person -1, values = people who trust them

        trusters = [ False ]* n

        for truster, trustee in trust:
            trusters[ truster - 1 ] = True
            
            trusts[trustee-1].append(truster)

        print(trusts)
        print(trusters)
        for i, isTrust in enumerate(trusters):
            if not isTrust and len(trusts[i]) == n-1:
                return i+1
        return -1
        

        