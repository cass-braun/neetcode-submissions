class Solution:
    def calPoints(self, operations: List[str]) -> int:
        data = []

        for o in operations:
            
            if o == '+':
                s1 = data.pop()
                s2 = data.pop()

                data.append(s2)
                data.append(s1)
                
                data.append(int(s1+s2))
            elif o == 'D':
                s = int(data.pop())
                data.append(s)

                data.append(2*s)
            elif o == 'C':
                data.pop()
            else:
                data.append(int(o))
        
        return sum(data)