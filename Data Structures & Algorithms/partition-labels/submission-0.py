class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIndex = {}

        for i, char in enumerate(s):
            maxIndex[char] = i

    
        substringLengths = []
        end = 0
        currentLength = 0
        
        for i, char in enumerate(s):
            currentLength += 1
            end = max(end, maxIndex[char])

            if i == end:
                substringLengths.append(currentLength)
                currentLength = 0
                end = i
        
        return substringLengths