class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def dfs(n,visited):
            if n == 1 or n == 10 or n == 100:
                return True
            if n in visited:
                return False
            visited.add(n)
            return dfs((n//10)**2 + (n%10)**2,visited)

        return dfs(n,visited)