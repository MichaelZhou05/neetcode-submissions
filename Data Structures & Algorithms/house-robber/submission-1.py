class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0] * len(nums) 
        l = len(nums)
        if l<3 :
            return max(nums[0], nums[1] if len(nums)>0 else 0)
            
        money[l-1],money[l-2]= nums[l-1], nums[l-2]
        money[l-3] = nums[l-3] + nums[l-1]

        for i in range(l-4, -1, -1) :
            money[i] = nums[i] + max(money[i+2], money[i+3])
            print(money)
        

        return max(money[0], money[1])