class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp1 = defaultdict(list)

        ret = True

        for a,b in prerequisites:
            mp1[a].append(b)
        

        def dfs(s1, course):
            nonlocal ret

            if course in s1:
                ret = False
                return

            if course not in mp1:
                return
            
            s1.add(course)
            for x in mp1[course]:
                dfs(s1,x)
            


        for course in mp1.keys():
            dfs(set(),course)
        
        return ret

            