class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        components = path.split('/')

        for c in components:
            if c == '' or c == '.':
                continue
            elif c ==  '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
            
        return '/' + '/'.join(stack)
