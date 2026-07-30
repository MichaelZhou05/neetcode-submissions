class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]

        for i in range(len(intervals)) :
            if intervals[i][1] >= start and intervals[i][1] <= end :
                start = min(start, intervals[i][0])
                intervals.remove(subList)
            elif intervals[i][0] >= start and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                intervals.remove(subList)
                intervals.insert(i,[start,end])
            

        if [start, end] not in intervals: 
            i = 0
            while i < len(intervals) and intervals[i][0] < start:
                i += 1
            intervals.insert(max(0,i),[start,end])
           
        
        return intervals
            
