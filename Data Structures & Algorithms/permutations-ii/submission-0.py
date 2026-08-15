class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:    
        n = len(nums)
        ret = []
        ret.append(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i] != nums[j]:
                    nums[i],nums[j] = nums[j], nums[i]
                    ret.append(nums[:])
                    nums[i],nums[j] = nums[j], nums[i]
        
        return ret
