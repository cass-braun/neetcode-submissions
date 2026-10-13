class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == window_count:
            return True

        for i in range(len1, len2):
            window_count[ord(s2[i]) - ord('a')] += 1

            window_count[ord(s2[i - len1]) - ord('a')] -= 1
            if s1_count == window_count:
                return True
        
        return False