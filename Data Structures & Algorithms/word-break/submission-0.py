class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        canWord = [False]*(len(s) +1)

        canWord[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                startWord = s[0:j]
                endWord = s[j:i]

                if canWord[j] and s[j:i] in word_set:
                    canWord[i] = True
                    break
        
        return canWord[len(s)]

