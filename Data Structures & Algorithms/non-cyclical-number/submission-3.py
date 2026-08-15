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
            first = n%10
            n = n //10
            second = n%10
            n = n//10
            thrid = n%10
            return dfs((first)**2 + (second)**2 + (thrid)**2)

        return dfs(n)