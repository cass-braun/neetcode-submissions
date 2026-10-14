class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def p(i, subsection, comb):
            if len(subsection) == 0:
                res.append(comb.copy())
                return

            for j in range(len(subsection)):
                jval = subsection.pop(j)
                comb.append(jval)

                p(j, subsection, comb)

                comb.pop(len(comb)-1)
                subsection.insert(j, jval)

        p(0, nums, [])
        return res
