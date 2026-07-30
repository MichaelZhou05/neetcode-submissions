"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        lastEnd = 0
        nxtDay = []
        i=0
        days = 0
        while len(intervals):
            while i < len(intervals) :
                if intervals[i].start < lastEnd:
                    print("skipped ->" + str(intervals[i].start) + str(intervals[i].end))
                    nxtDay.append(intervals[i])
                    intervals.pop(i)
                    i-=1
                lastEnd = max(lastEnd,intervals[i].end)
                print("lastEnd =" + str(lastEnd))
                i += 1
            intervals = nxtDay.copy()
            nxtDay = []
            days += 1
            lastEnd = 0
        
        return days
            

