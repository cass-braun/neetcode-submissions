class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] +=1

        for n, c in d.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



