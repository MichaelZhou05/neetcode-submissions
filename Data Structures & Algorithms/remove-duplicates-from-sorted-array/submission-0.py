class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #[2,10,30,10,30,30]
        #       ^           ^
        #offset = 0


        # [1,2,3,4,1]
        #        ^   ^
        #  offset = 1

        offset=0
        for i in range(len(nums)-1):
            j=i+1+offset
            while j< len(nums) and nums[j] == nums[i]:
                offset += 1
                j+=1
            if j >= len(nums): return i+1
            nums[i+1], nums[j] = nums[j], nums[i+1]

        
        return len(nums)-offset