class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        hs1, hs2 = defaultdict(int), defaultdict(int)
        if len(s1) > len(s2) : return False

        for i, n in  enumerate(s1):
            hs1[n] +=1
            hs2[s2[i]] += 1

        for i in range(k,len(s2)) :
            if hs1 == hs2 :
                return True
            print(hs1)
            print(hs2)
            if hs2[s2[i-k]] >1 : hs2[s2[i-k]] -= 1
            else: del hs2[s2[i-k]]
            hs2[s2[i]] += 1
        
        return False



            

