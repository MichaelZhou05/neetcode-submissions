class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # [1,2,4,5,6,3,1]
        #  
        # max = 1
        # total


        for i,val in enumerate(nums):
            if val < 0 :
                nums[i] = 0
        

        for i,val in enumerate(nums):
            if abs(val)-1 >= 0 and abs(val)-1 < len(nums):
                nums[abs(val)-1] = -1 * abs(nums[abs(val)-1])
                if nums[abs(val)-1] == 0 : nums[abs(val)-1] -= 1
        
        for i,val in enumerate(nums):
            if val >=0:
                return i+1
        
        return 1+len(nums)

