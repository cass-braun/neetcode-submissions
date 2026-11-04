class Solution:
    def calPoints(self, operations: List[str]) -> int:
        data = []

        for o in operations:
            
            if o == '+':
                s1 = data[-1]
                s2 = data[-2]
                
                data.append(int(s1+s2))
            elif o == 'D':
                s = data[-1]

                data.append(2*s)
            elif o == 'C':
                data.pop()
            else:
                data.append(int(o))
        
        return sum(data)