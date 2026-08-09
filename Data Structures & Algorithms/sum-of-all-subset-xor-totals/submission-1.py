class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        curr = []
        ret = 0

        for i,val in enumerate(nums):
            ret += val
            temp = []
            for total in curr:
                ret += total ^ val
                temp.append(total ^ val)
            curr += temp
            curr.append(val)

        return ret

        
        
        # ret = 0
        # for n in range(len(nums)):
        #     i = 0
        #     while i+n < len(nums):
        #         add = 0
        #         for j in range(i,i+n+1):
        #             print(i)
        #             print(n)
        #             print(j)
        #             add = add ^ nums[j]
        #             print("add")
        #             print(add)
        #         ret += add
        #         i += 1
        
        # return ret

        #1
        #3
        #31
        #311,31,11,1