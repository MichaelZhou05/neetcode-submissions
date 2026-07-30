class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp1 = defaultdict(int)

        for a,b in edges:
            mp1[a]+=1
            mp1[b]+=1
            if mp1[a] > 3 or mp1[b] > 3:
                return False
        
        return True