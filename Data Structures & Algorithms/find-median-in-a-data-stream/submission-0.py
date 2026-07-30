class MedianFinder:

    def __init__(self):
        self.bot = [float("inf")] #all negative values
        self.top = [float("inf")]

        heapq.heapify(self.bot)
        heapq.heapify(self.top)



        

        

    def addNum(self, num: int) -> None:
        if (len(self.bot) + len(self.top)) % 2 == 0: 
            if num < self.top[0] :
                heapq.heappush(self.bot, -num)
            else:
                med = heapq.heappop(self.top)
                heapq.heappush(self.top,num)
                heapq.heappush(self.bot,-med)
        else:
            if num > -self.bot[0] :
                heapq.heappush(self.top,num)
            else: 
                med = -heapq.heappop(self.bot)
                heapq.heappush(self.top, med)
                heapq.heappush(self.bot,-num)
        
        

    def findMedian(self) -> float:
        if len(self.bot) + len(self.top) == 2:
            return None

        if (len(self.bot) + len(self.top)) % 2 == 0:
            l,r = self.bot[0], self.top[0]
            return (-l + r)/2
        else :
            return -self.bot[0]
        
        