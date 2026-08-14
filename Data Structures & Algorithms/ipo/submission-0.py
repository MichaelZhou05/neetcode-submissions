class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        for i in range(len(capital)):
            projects.append([capital[i],profits[i]])
        projects.sort(key = lambda x: x[0])
        
        i = 0
        available = []
        while k:
            while i<len(projects) and projects[i][0] <= w:
                heapq.heappush(available,-1*projects[i][1])
                i += 1
            w+= -1 * heapq.heappop(available)
            k-=1
        return w

        


        

        # if profit[i] <= captial[i] don't do

        #Exampl1:
        #k=3, 2, 1, 0
        #w=0, 1, 4, 8
        #avaible options is everything cpatial[i] < w

