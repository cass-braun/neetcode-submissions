class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for p, s, e in trips:
            heapq.heappush(events, (s, p))
            heapq.heappush(events, (e, -p))

        d = 0
        currP = 0
        while events:
            while events and events[0][0] == d:
                _, p = heapq.heappop(events)
                currP += p
                if currP > capacity:
                    return False
            d += 1
        
        return True