class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []

        for s in strs:
            final.append(str(len(s)))
            final.append('#')
            final.append(s)
            
        return ''.join(final)
    
    def decode(self, s: str) -> List[str]:
        results = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            
            length = int(s[i:j])

            start = j+ 1
            end = start + length
            word = s[start:end]
            results.append(word)

            i = end
        
        
        return results