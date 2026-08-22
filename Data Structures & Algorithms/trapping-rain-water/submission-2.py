class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n

        left = 0
        for i in range(n):
            left = max(left,height[i])
            maxL[i] = left

        
        right = 0
        for i in range(n-1,-1,-1):
            right = max(right,height[i])
            maxR[i] = right
        
        ret = 0



        for i in range(1,n-1):
            ret += max(min(maxL[i-1],maxR[i+1])-height[i],0)
        
        return ret