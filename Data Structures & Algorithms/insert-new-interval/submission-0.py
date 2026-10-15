class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        nIntervals = []
        while 0 <= i < len(intervals):
            interval = intervals[i]

            startSandwich = newInterval[0] <= interval[1] and newInterval[0] >= interval[0]
            endSandwich = newInterval[1] <= interval[1] and newInterval[1] >= interval[0]

            if newInterval[0] > interval[1]: # new interval strictly higher than current interval, pass/continue searching for its spot 
                nIntervals.append(interval)

            elif newInterval[1] < interval[0]: # new interval strictly lower than current interval, insert at index and return new intervals
                nIntervals.append(newInterval)
                for j in intervals[i:]:
                    nIntervals.append(j)
                return nIntervals
            
            
            elif startSandwich or endSandwich: # start is sandwiched or end
                if startSandwich and endSandwich:
                    newInterval = [interval[0],interval[1]]
                elif startSandwich:
                    # merge intervals
                    newInterval = [interval[0],newInterval[1]]
                elif endSandwich:
                    newInterval = [newInterval[0],interval[1]]

            i+=1
        
        nIntervals.append(newInterval)

        return nIntervals
            