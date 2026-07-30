class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        maxL, maxR = height[l], height[r]
        res=0

        while l<r :
            if height[l] < height [r] :
                l += 1
                h = height[l]
                res += max(min(maxL,maxR) - h,0)
                maxL = max(maxL, h)
            else :
                r -= 1
                h = height[r]
                res += max(min(maxL,maxR) - h,0)
                maxR = max(maxR, h)

        
      
        return res