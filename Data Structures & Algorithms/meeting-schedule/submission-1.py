"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)

        endTime = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start >= endTime:
                endTime = interval.end
            else:
                return False
        return True




