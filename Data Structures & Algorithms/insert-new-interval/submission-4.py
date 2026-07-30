class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
    
        for i, subList  in enumerate(intervals):
            if subList[0] <= start and subList[1] >= end:
                print("not inserted")
                return intervals

            elif subList[1] >= start and subList[1] <= end :
                start = min(start, subList[0])
                print(start, end)
                intervals.remove(subList)
                print(intervals)

        for i, subList  in enumerate(intervals):
            if subList[0] >= start and subList[0] <= end:
                print(start, end)
                end = max(end, subList[1])
                intervals.remove(subList)
                print(intervals)


        intervals.insert(i,[start,end])
           
        
        return intervals
            
