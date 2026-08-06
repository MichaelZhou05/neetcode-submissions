class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float('inf')         

        l,r = 0,0
        currSum = nums[0]

        while True:
            if currSum < target:
                r += 1
                if r >= len(nums):
                    return ret if ret < float('inf') else 0
                currSum += nums[r]
            else:
                ret = min(ret, r-l+1)
                currSum -= nums[l]
                l+=1
        
        return -1