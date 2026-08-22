class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        minSum = r
        def canMake(maxSubVal,k):
            currSum = 0
            for val in nums:
                currSum += val
                if currSum > maxSubVal:
                    k-=1
                    currSum = val
            
            return k >= 0
        while l<r:
            mid = (l+r)//2
            if canMake(mid,k):
                minSum = r
                r = mid -1
            else:
                l = mid + 1



                

