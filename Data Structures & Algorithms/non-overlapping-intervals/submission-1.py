class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ret = []
        count = 0

        for i, sublist in enumerate(intervals):
            start, end = sublist[0], sublist[1]

            if i+1 < len(intervals) and intervals[i+1][0] < end:
                intervals.remove(max(sublist, intervals[i+1], key = lambda x: x[1]))
                count += 1
                i =- 1
        
        return count
