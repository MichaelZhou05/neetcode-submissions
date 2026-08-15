class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def reccur(ls1)  -> List[List[int]]:
            if not len(ls1) :
                return [[]]

            retList = reccur(ls1[1:])
            ret = []
            val = ls1[0]
            for i in retList:
                for j in range(len(i)):
                    icpy = i.copy()
                    icpy.insert(j,val)
                    ret.append(icpy)
                i.append(val)
                ret.append(i)
            
            return ret

        return reccur(nums)
                



            

