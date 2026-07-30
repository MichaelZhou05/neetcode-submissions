class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = max(nums)

        lMax, lMin = 1, 1

        for x in nums :
            temp = lMax
            lMax = max(lMax * x, lMin*x, x)
            lMin = min(temp * x, x*lMin, x)
            ret = max(ret,lMax)

        return ret
            
        