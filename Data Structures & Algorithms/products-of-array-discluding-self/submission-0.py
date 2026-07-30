class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None] * len(nums) 
        suf = [None] * len(nums)
    
        pre[0] = nums[0]
        suf[len(nums) -1] = nums[len(nums)-1]

        for i in range(1,len(nums)) :
            pre[i] = pre [i-1] * nums [i]
            suf[len(nums) - 1 - i] = nums[len(nums) - 1 - i] * suf[len(nums) - i]

        suf.reverse()
        print(pre)
        print(suf)
        
        ret = [None] * len(nums)
        ret[0] = suf[len(nums) -2]
        ret[len(nums)-1] = pre[len(nums)-2]
        for i in range(1, len(nums) - 1) :
            ret[i] = pre[i-1] * suf[len(nums) - 2 - i]
        
        return ret