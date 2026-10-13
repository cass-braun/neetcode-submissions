class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        for s in strs:
            key = [0]* 26

            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1

            key = tuple(key)

            if key not in mydict:
                mydict[key] = []
            
            mydict[key].append(s)


        result = []

        for v in mydict.values():
            result.append(v)

        return result