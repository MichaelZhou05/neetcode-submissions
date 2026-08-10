from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowInDegree = [0 for _ in range(k+1)]
        colInDegree = [0 for _ in range(k+1)]
        rowAdj = defaultdict(list)
        colAdj = defaultdict(list)

        for a,b in rowConditions:
            rowAdj[a].append(b)
            rowInDegree[b] += 1
        
        for a,b in colConditions:
            colAdj[a].append(b)
            colInDegree[b] += 1


        rowposition = defaultdict(int) #val [1,k] -> row
        colposition = defaultdict(int) #val [1,k] -> col

        rowVisited = set()
        colVisited = set()

        rowQue = deque([])
        for r in range(1,k+1):
            if rowInDegree[r] == 0:
                rowQue.append(r)

        index = 0
        while rowQue:
            r = rowQue.popleft()
            
            rowVisited.add(r)
            rowposition[r] = index
            index += 1
            for adj in rowAdj[r]:
                rowInDegree[adj] -= 1
                if rowInDegree[adj] == 0:
                    rowQue.append(adj)
        
        if len(rowVisited) < k:
            return []

        colQue = deque([])
        for c in range(1,k+1):
            if colInDegree[c] == 0:
                colQue.append(c)

        index = 0
        while colQue:
            c = colQue.popleft()
            if c in colVisited:
                return []
            
            colVisited.add(c)
            colposition[c] = index
            index += 1
            for adj in colAdj[c]:
                colInDegree[adj] -= 1
                if colInDegree[adj] == 0:
                    colQue.append(adj)
        
        if len(colVisited) < k:
            return []


        ret = [[0 for _ in range(k)]for _ in range(k)]

        for i in range(1,k+1):
            r,c = rowposition[i], colposition[i]
            ret[r][c] = i
        
        return ret