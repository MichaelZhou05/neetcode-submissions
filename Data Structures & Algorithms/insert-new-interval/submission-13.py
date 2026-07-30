class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        ret = []
        i = 0
        while i < len(intervals) :
            if intervals[i][0] <= start and intervals[i][1] >= end:
                print("not inserted")
                return intervals
            
            if intervals[i][1] >= start and intervals[i][1] <= end :
                start = min(start, intervals[i][0])

            elif intervals[i][0] >= start and intervals[i][0] <= end:
                end = max(end, intervals[i][1])

            else:
                ret.append(intervals[i])
            i += 1 
        i=0
        while i< len(ret) and ret[i][0] < start:
            i+=1

        ret.insert(i, [start,end])

           
        
        return ret
            
