"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not len(intervals):
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, intervals[0].end) #first meetings end time

        maxRooms = 1
       
        i = 1
        while i<len(intervals) :
            start, end = intervals[i].start, intervals[i].end
            if start < heap[0]:
                heapq.heappush(heap,end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,end)
            i += 1
        
        return len(heap)
        






