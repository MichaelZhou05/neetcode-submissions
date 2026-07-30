class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp1 = defaultdict(list)
        dp = set()

        for a,b in prerequisites:
            mp1[a].append(b)
        
        s1 = set()

        def dfs(course) -> bool:
            nonlocal s1
            if course in s1:
                return False

            if course in dp or course not in mp1 :
                dp.add(course)
                return True
            
            
            s1.add(course)
            for x in mp1[course]:
                if not dfs(x):
                    return False
            s1.remove(course)
            dp.add(course)
            return True


        for course in mp1.keys():
            if not dfs(course):
                return False

        return True