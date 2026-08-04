from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(set)
        revList = defaultdict(set)
        outdegree = defaultdict(int)
        for ai,bi in prerequisites:
            adjList[bi].add(ai)
            revList[ai].add(bi)
            outdegree[bi]+= 1

        que = deque([])
        for node in range(numCourses):
            if outdegree[node] == 0:
                que.append(node)

        while que:
            node = que.popleft()
            for parent in revList[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    que.append(parent)
                adjList[parent] = adjList[parent].union(adjList[node])



        ret = []
        for uj,vj in queries:
            if uj in adjList[vj]:
                ret.append(True)
            else:
                ret.append(False)
            

        return ret
        

        