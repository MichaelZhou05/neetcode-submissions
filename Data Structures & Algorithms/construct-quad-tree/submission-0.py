"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        def dfs(grid):
            n = len(grid)
            total = 0
            for row in grid:
                for num in row:
                    total += num

            if total == n*n:
                isLeaf = True
                val = 1
                return Node(val,isLeaf,None,None,None,None)
            elif total == 0:
                isLeaf = True
                val = 0
                return Node(val,isLeaf,None,None,None,None)
            
            #not true all same num --> break into 4

            half = int(n/2)
            print(n)
            print(half)
            topLeft = dfs([row[0:half] for row in grid[0:half]])
            topRight = dfs([row[half::] for row in grid[0:half]])
            botLeft = dfs([row[0:half] for row in grid[half::]])
            botRight = dfs([row[half::] for row in grid[half::]])

            return Node(1,0,topLeft, topRight, botLeft, botRight)

            

        return dfs(grid)