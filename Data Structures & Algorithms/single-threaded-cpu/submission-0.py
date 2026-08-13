class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #sort tasks by start time to avoid idle time
        #while startime of next task is < cpu busy until -> enque the tasks (heap sort by pr[pocessTime & index])
        #cpu task ques the next task

        hq = []
        for i, [enqueue, time] in enumerate(tasks):
            heapq.heappush(hq,[enqueue,time,i])

        
        
        cpuBusy = 0
        waitingTasks = []
        ret = []
        while hq:
            queTime,processTime,index = heapq.heappop(hq)
            if queTime > cpuBusy:
                while waitingTasks and cpuBusy < queTime:
                    nextPT, i = heapq.heappop(waitingTasks)
                    cpuBusy += nextPT
                    ret.append(i)
                cpuBusy = max(cpuBusy,queTime)        
            heapq.heappush(waitingTasks,[processTime,index])

        while waitingTasks:
            nextPT, i = heapq.heappop(waitingTasks)
            cpuBusy += nextPT
            ret.append(i)
            
        return ret