class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        for val in nums:
            res = res | val
        

        return  res << (len(nums)-1)