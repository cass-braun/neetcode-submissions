class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen(s, numClose, numOpen):
            if len(s) == n*2:
                res.append(s)
            if numOpen < n:
                newS = s + '('
                gen(newS, numClose, numOpen+1)
            if numOpen > numClose:
                gen(s + ')', numClose+1, numOpen)
    
        gen('', 0,0)

        return res