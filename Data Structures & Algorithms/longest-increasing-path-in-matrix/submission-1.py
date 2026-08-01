class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        delta = [[-1,0],[1,0],[0,1],[0,-1]]
        
        valToIndex = defaultdict(list)
        m,n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                valToIndex[matrix[r][c]].append([r,c])

        valList = list(valToIndex)
        valList.sort()

        dp = [[1 for _ in range(n)] for _ in range(m)]
        ret = 1
        for val in valList:
            for r,c in valToIndex[val]:
                for dr,dc in delta:
                    if r+dr<m and r+dr >= 0 and c+dc < n and c+dc >= 0 and matrix[r+dr][c+dc] < matrix[r][c]:
                        dp[r][c] = max(dp[r][c],1 + dp[r+dr][c+dc])
                        ret = max(ret,dp[r][c])
        

        return ret

                    
