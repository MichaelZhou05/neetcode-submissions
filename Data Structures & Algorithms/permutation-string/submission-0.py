class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        hs1, hs2 = set(), set()

        for i, n in  enumerate(s1):
            hs1.add(n)
            hs2.add(s2[i])

        for i in range(k,len(s2)) :
            if hs1 == hs2 :
                return True
            if s2[i-k] in hs2 : hs2.remove(s2[i-k])
            hs2.add(s2[i])
        
        return False



            

