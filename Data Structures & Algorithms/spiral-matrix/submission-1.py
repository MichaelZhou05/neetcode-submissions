class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def right(r,c,matrix):
            nonlocal visited
            if c >= len(matrix[0]) or (r,c) in visited:
                return (r,c-1)
            visited.add((r,c))
            nonlocal ret
            ret.append(matrix[r][c])
            return right(r,c+1,matrix)
        
        def left(r,c,matrix):
            nonlocal visited
            if c <0 or (r,c) in visited:
                return (r,c+1)
            visited.add((r,c))
            nonlocal ret
            ret.append(matrix[r][c])

            return left(r,c-1,matrix)
        
        def down(r,c,matrix):
            nonlocal visited
            if r >= len(matrix) or (r,c) in visited:
                return  (r-1,c)
            visited.add((r,c))
            nonlocal ret
            ret.append(matrix[r][c])
            return down(r+1,c,matrix)
        
        def up(r,c,matrix):
            nonlocal visited
            if r < 0 or (r,c) in visited:
                return (r+1,c)
            visited.add((r,c))
            nonlocal ret
            ret.append(matrix[r][c])
            return up(r-1,c,matrix)
        


        visited = set()
        ret = []
        m,n = len(matrix),len(matrix[0])
        r,c = 0,-1
        while len(visited) < m*n:
            print(ret)
            r,c = right(r,c+1,matrix)
            r,c = down(r+1,c,matrix)
            r,c = left(r,c-1,matrix)
            r,c = up(r-1,c,matrix)
        
        return ret