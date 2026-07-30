class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp1 = defaultdict(list)

        for a,b in edges :
            mp1[a].append(b)
            mp1[b].append(a)
        
        vist = set()
        def dfs(node, prev):
            if node in vist :
                return False
            
            vist.add(node)
            for x in mp1[node]:
                if x == prev:
                    continue
                if not dfs(x,node):
                    return False
            return True
        
        return dfs(0,None) and len(vist) == n
