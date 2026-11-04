class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0
        
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                # Push the current state onto the stack and reset
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif c == ']':
                # Pop the previous string and the multiplier
                prev_str, k = stack.pop()
                # Multiply current string and combine with previous string
                cur_str = prev_str + cur_str * k
            else:
                # It's a regular letter
                cur_str += c
                
        return cur_str