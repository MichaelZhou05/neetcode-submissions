class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret = []
        dp = set()
        isPossible = True
        mp1 = defaultdict(list)
        for a,b in prerequisites:
            mp1[a].append(b)
        
        visited = set()
        
        def dfs(course):
            nonlocal ret
            if course in visited:
                nonlocal isPossible
                isPossible = False  #loop --> return empty array
                return 
            
            if course in dp:
                return

            if course not in mp1: # no pre-req --> Take calss
                ret.append(course)
                return
            
            visited.add(course)
            for x in mp1[course]: #has pre-req --> visit pre-req
                dfs(x)
            ret.append(course)
            dp.add(course)
            visited.remove(course)
        

        for x in mp1:
            dfs(x)

        for i in range(numCourses - len(ret)) :
            ret.append(len(ret))

        
        return ret if isPossible else []



