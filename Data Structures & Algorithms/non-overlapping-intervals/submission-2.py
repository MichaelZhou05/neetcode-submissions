class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ret = []
        count = 0

        i = 0
        while i< len(intervals):
            start, end = intervals[i][0], intervals[i][1]

            if i+1 < len(intervals) and intervals[i+1][0] < end:
                intervals.remove(max(intervals[i], intervals[i+1], key = lambda x: x[1]))
                count += 1
                i =- 1
            i += 1
        
        return count
