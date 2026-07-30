class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for ui, vi, ti in times:
            graph[ui].append((vi,ti))
        
        visited = set()
        hq =[]
        heapq.heappush(hq, [0,k])
        #heap [time to curr, node #]

        minDelay = float('-inf')

        while hq:
            currDelay, ui = heapq.heappop(hq)
            if ui in visited:
                continue
            minDelay = max(minDelay,currDelay)

            for vi, ti in graph[ui]:
                if vi not in visited:
                    heapq.heappush(hq, [currDelay + ti, vi])
            
            visited.add(ui)

        return minDelay if len(visited) == n else -1
        