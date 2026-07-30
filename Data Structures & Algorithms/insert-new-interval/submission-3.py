class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        index = float("inf")

        for i, subList  in enumerate(intervals):
            if subList[0] <= start and subList[1] >= end:
                print("not inserted")
                return intervals
            elif subList[0] >= start and subList[0] <= end:
                end = max(end, subList[1])
                intervals.remove(subList)
                index = min(index, i)
            elif subList[1] >= start and subList[1] <= end :
                start = min(start, subList[0])
                intervals.remove(subList)
                index = min(index, i)
        
        intervals.append([start,end], index)
        return intervals
            
