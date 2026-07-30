class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp1 = defaultdict(list)
        for a,b in edges:
            mp1[a].append(b)
            mp1[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in mp1[node]:
                dfs(i)
        
        count = 0            
        for x in range(n):
            if x not in visited:
                count+=1
                dfs(x)
        return count
            
