class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        s1 = defaultdict(int)
        for i in tasks : 
            s1[i] += 1
        
        heap = []
        for i in s1 :
            heap.append(-s1[i])
        heapq.heapify(heap)
        print(heap)
        
        que = []
        time = 0
        while heap or que :
            if que and time == que[0][1]: 
                val = que.pop(0)[0]
                heapq.heappush(heap, val)
            if heap: 
                num = heapq.heappop(heap)
                num += 1
                if num < 0 :
                    que.append([num, time + 1+ n])
            time += 1
        
        return time


            

           
           



        

