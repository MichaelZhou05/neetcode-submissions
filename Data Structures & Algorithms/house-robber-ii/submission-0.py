class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {} #index -> max 

        
        def dfs(flag, index) -> int:
            if index >= len(nums) :
                return 0    
            
            if index + 3 == flag:
                return nums[index] + nums[index+2]
            
            if (index+3) % len(nums) == flag:
                return nums[index] + nums[(index+2) % len(nums)]

            if index + 2 == flag or (index + 2) % len(nums) == flag :
                return nums[index]

            if index + 1 == flag or (index + 1) % len(nums) == flag :
                return nums[index]
            
            if index in cache:
                return cache[index]
            
            cache[index] = nums[index] + max(dfs(flag,index+2), dfs(flag,index+3))
            return cache[index]

        
    

        return max(dfs(len(nums)-1,0),dfs(0,1),dfs(1,2))
        