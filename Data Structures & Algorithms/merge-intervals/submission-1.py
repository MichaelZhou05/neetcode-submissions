class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        start, end = intervals[0][0], intervals[0][1]

        for i, sublist in enumerate(intervals):
            if sublist[0] <= end: 
                end = max(end, sublist[1])
            else:
                ret.append([start,end])
                start,end = sublist[0], sublist[1]

            i += 1

        ret.append([start,end]) 
        return ret
            

            


