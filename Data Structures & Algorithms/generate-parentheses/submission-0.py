class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []



        def reccur(opeN, closE, str1) :
            if opeN > n or closE > n : 
                return
            elif opeN == n and closE == n :
                result.append(str1)
                return
            
            if closE < opeN :
                reccur(opeN, closE+1, str1+")")
            if opeN < n :
                reccur(opeN + 1, closE, str1+"(")
        
        reccur(0,0,"")
        return result

            


        
        
        
            