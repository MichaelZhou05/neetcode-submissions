class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        delta = [[-1,0],[1,0],[0,1],[0,-1]]
        m,n = len(matrix), len(matrix[0])

        indegree = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for dr,dc in delta:
                    if r+dr<m and r+dr >= 0 and c+dc < n and c+dc >= 0 and matrix[r+dr][c+dc] < matrix[r][c]:
                        if matrix[r+dr][c+dc] < matrix[r][c]:
                            indegree[r][c] += 1
        
        que = []
        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    que.append([r,c])
        
        ret = 0
        while que:
            nextQue =[]
            for r,c in que:
                for dr,dc in delta:
                    if r+dr<m and r+dr >= 0 and c+dc < n and c+dc >= 0:
                        if matrix[r+dr][c+dc] > matrix[r][c]:
                            indegree[r+dr][c+dc] -= 1
                            if indegree[r+dr][c+dc] == 0 : nextQue.append([r+dr,c+dc])
            
            que = nextQue
            ret += 1
        
        return ret



                