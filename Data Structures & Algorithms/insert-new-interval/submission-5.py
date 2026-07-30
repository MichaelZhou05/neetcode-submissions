class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]

        for i, subList  in enumerate(intervals):
            if subList[1] >= start and subList[1] <= end :
                start = min(start, subList[0])
                intervals.remove(subList)
            
        for i, subList  in enumerate(intervals):
            if subList[0] >= start and subList[0] <= end:
                end = max(end, subList[1])
                intervals.remove(subList)
                intervals.insert(i,[start,end])
            

        if [start, end] not in intervals: 
            i = 0
            while intervals[i][0] < start:
                i += 1
            intervals.insert(i,[start,end])
           
        
        return intervals
            
