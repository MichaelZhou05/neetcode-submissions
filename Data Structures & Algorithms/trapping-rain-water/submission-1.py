class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n

        left = 0
        for i in range(height):
            left = max(left,height[i])
            maxL[i] = left

        
        right = 0
        for i in range(n-1,-1,-1):
            rigt = max(right,height[i])
            maxL[i] = right