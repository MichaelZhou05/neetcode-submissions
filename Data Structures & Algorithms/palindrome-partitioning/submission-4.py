class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
    
        def dfs(index, ls1):
            if index >= len(s) :
                for x in ls1:
                    if not isPali(x):
                        return
                ret.append(ls1)
                return
            ls1.append(s[index])
            dfs(index+1, ls1[:])
            ls1.pop()
            ls1[-1] = ls1[-1] + s[index]
            print(ls1)
            dfs(index+1, ls1[:])


        def isPali(str1) -> bool:
            for i in range(len(str1)//2) :
                if str1[-1 - i] != str1[i] :
                    return False
            return True

        
        dfs(1, [s[:1]])
        return ret
        