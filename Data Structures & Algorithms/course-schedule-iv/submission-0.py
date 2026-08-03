class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(set)
        reverseList = defaultdict(set)
        for ai,bi in prerequisites:
            adjList[bi].add(ai)
            reverseList[ai].add(bi)
            for course in reverseList[bi]:
                adjList[course].add(ai)
        
        print(adjList)
        print(reverseList)

        ret = []
        for uj,vj in queries:
            if uj in adjList[vj]:
                ret.append(True)
            else:
                ret.append(False)
            

        return ret
        

        