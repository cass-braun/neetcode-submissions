class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Precompute multiplication table: multiply[carry][i][j] = str(i * j + carry)
        multiply = {}
        for k in range(10):
            multiply[str(k)] = {}
            for i in range(10):
                multiply[str(k)][str(i)] = {}
                for j in range(10):
                    multiply[str(k)][str(i)][str(j)] = str(i * j + k)
                    
        # Precompute addition table: add[carry][i][j] = str(i + j + carry)
        add = {}
        for k in range(2):
            add[str(k)] = {}
            for i in range(10):
                add[str(k)][str(i)] = {}
                for j in range(10):
                    add[str(k)][str(i)][str(j)] = str(i + j + k)

        # Fixed adder function using right-to-left pointer traversal
        def adder(s1, s2):
            res = []
            i, j = len(s1) - 1, len(s2) - 1
            carry = '0'
            while i >= 0 or j >= 0 or carry != '0':
                d1 = s1[i] if i >= 0 else '0'
                d2 = s2[j] if j >= 0 else '0'
                val = add[carry][d1][d2]
                if len(val) == 2:
                    res.append(val[1])
                    carry = val[0]
                else:
                    res.append(val[0])
                    carry = '0'
                i -= 1
                j -= 1
            return "".join(reversed(res))

        total = "0"
        n1_len = len(num1)
        
        # Main multiplication loop
        for i in range(n1_len - 1, -1, -1):
            carry = '0'
            temp_res = []
            for j in range(len(num2) - 1, -1, -1):
                val = multiply[carry][num1[i]][num2[j]]
                if len(val) == 2:
                    temp_res.append(val[1])
                    carry = val[0]
                else:
                    temp_res.append(val[0])
                    carry = '0'
            
            if carry != '0':
                temp_res.append(carry)
            
            # Reverse to get the correct digit order for this row
            row_str = "".join(reversed(temp_res))
            
            # Shift the row based on its place value (e.g., tens, hundreds place)
            shift = n1_len - 1 - i
            row_str += '0' * shift
            
            total = adder(total, row_str)
            
        return total