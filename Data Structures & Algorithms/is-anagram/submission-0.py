class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [0]*26

        for i in s:
            index = ord(i) - ord('a')
            s_arr[index] += 1

        for j in t:
            a = ord(j) - ord('a')
            s_arr[a] -= 1
            
        return all(x == 0 for x in s_arr)