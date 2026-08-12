class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        hq = []
        for key,val in count.items():
            heapq.heappush(hq,[-1*val,key])
        
        ret = ""
        while len(hq) > 1 :
            count1, char1 = heapq.heappop(hq)
            count2, char2 = heapq.heappop(hq)
            count1 *= -1
            count2 *= -1
            ret = ret + char1 + char2
            if count1 -1 > 0 :
                count1 *= -1
                heapq.heappush(hq,[count1+1 ,char1])
            if count2 -1 > 0 :
                count2 *= -1
                heapq.heappush(hq,[count2+1 ,char2])
        if hq: 
            ret += heapq.heappop(hq)[1]
        
        return ret if len(ret) == len(s) else ""
            