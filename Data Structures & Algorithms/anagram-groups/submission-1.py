class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}

        for i, s in enumerate(strs):
            letterFreq = [0]*26
            for c in s:
                index = ord(c)- ord('a')
                letterFreq[index] += 1

            letterFreq = tuple(letterFreq)
            
            if letterFreq not in myDict:
                myDict[letterFreq] = []
            
            myDict[letterFreq].append(s) 
        
        res = []
        for arr in myDict.values():
            current = []
            for item in arr:
                current.append(item)
            
            res.append(current)
    
        return res
