class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            start = 0
            end = len(s) -1

            while start < end and s[start] == s[end]:
                start += 1
                end -=1
            
            return start == end or (start - end == 1 and s[start] == s[end]) 

        def p(curr, ps, endCurrIndex):
            '''
            if curr is palindrome:
                add curr to prev, add prev to res
                pop curr from prev

            if curr is not palindrome:
                subdivide curr until you get a palindrome you can add to prev
                if you get a palindrome:
                    run p with the new palindrome
            '''
            if isPalindrome(curr):
                ps.append(curr)
                res.append(ps.copy())
                ps.pop()
            
            for i in range(1,endCurrIndex):
                newS = s[endCurrIndex-i:endCurrIndex]
                if(isPalindrome(newS)):
                    ps.append(newS)
                    p(curr[:endCurrIndex-i], ps, endCurrIndex-i)

                    ps.pop()
            
        p(s, [], len(s))
        return res
            

        