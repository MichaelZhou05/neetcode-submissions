class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
    
        def dfs(index, ls1):
            if index >= len(s) :
                if isPali(ls1[-1]):
                    ret.append(ls1)
                return
            ls1.append(s[index])
            if isPali(ls1[-1]):
                dfs(index+1, ls1[:])
            ls1.pop()
            ls1[-1]=ls1[-1]+s[index]
            dfs(index+1, ls1[:])


        def isPali(str1) -> bool:
            for i in range(len(str1)//2) :
                if str1[-1 + i] != str1[i] :
                    return False
            return True

        
        dfs(1, [s[:1]])
        return ret
        