class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDic ={}
        for i in s:
            myDic.update({i : myDic.get(i,0)+1})
        for i in t:
            myDic.update({i : myDic.get(i,0)-1})

        for i in myDic:
            if myDic.get(i) != 0 :
                return False
        return True
            
