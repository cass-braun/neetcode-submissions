class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(i, comb, target):
            if target == 0:
                res.append(comb.copy())
                return
            if target < 0:
                return

            for j in range(i, len(candidates)): 
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                comb.append(candidates[j])
                backtrack(j + 1, comb, target - candidates[j]) 
                comb.pop()
        
        backtrack(0, [], target)
        return res