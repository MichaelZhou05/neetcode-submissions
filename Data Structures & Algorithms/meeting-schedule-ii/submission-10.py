"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)


        rooms = [intervals[0].end]
        heapq.heapify(rooms)

        maxDays = 1
        
        i = 1
        while i<len(intervals):
            if intervals[i].start <= rooms[0]:
                heapq.heappush(rooms,intervals[i].end)
                maxDays = max(maxDays,len(rooms))
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms,intervals[i].end)
            
            i += 1
        

        return maxDays


