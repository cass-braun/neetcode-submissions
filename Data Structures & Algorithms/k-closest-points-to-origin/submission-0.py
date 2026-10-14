import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        mydict = {}

        for p in points:
            d = math.sqrt(p[0]**2 + p[1]**2)
            dists.append(d)

            if d not in mydict:
                mydict[d] = []
            mydict[d].append(p)

        heapq.heapify(dists)

        res = []

        for _ in range(k):
            d = heapq.heappop(dists)

            p = mydict[d].pop()

            res.append(p)

        return res
