class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def dfs(n):
            if n == 1 or n == 10 or n == 100:
                return True
            nonlocal visited
            if n in visited:
                return False
            visited.add(n)
            nextVal = 0
            while n>0:
                nextVal += (n%10) ** 2
                n = n //10
            return dfs((nextVal)**2)

        return dfs(n)