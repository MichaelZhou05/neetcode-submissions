class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighborsCount = [0 for _ in range(n)]
        adjList = defaultdict(list)
        for a,b in edges:
            neighborsCount[a] += 1
            neighborsCount[b] += 1
            adjList[a].append(b)
            adjList[b].append(a)
        
        que = []
        for i,count in enumerate(neighborsCount):
            if count == 1:
                que.append(i)
        visited = set()
        while que:
            if len(que) == n:
                return que
            nextLayer = set()
            for i in range(len(que)):
                node = que[i]
                if node in visited: continue
                visited.add(node)
                for nextNode in adjList[node]:
                    if nextNode not in nextLayer:
                        neighborsCount[nextNode] -= 1
                    if neighborsCount[nextNode] == 1:
                        nextLayer.add(nextNode)
            if len(nextLayer)+ len(visited) == n:
                return list(nextLayer)
            que = list(nextLayer)
        

        return [-1]