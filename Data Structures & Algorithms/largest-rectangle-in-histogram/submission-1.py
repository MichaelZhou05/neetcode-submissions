class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = max(heights)
        n = len(heights)



        # 7,1,7,2,2,4
        #         ^
        
        #stack = [1,0], [2,2]
        #lastHeight = 7
        #startingIndex = 2

        #area = 7

  
        for i,height in enumerate(heights):
            if not stack or height > stack[-1][0]:
                stack.append([height,i])
                continue
            
            if height == stack[-1][0]:
                continue

            lastIndex = 0
            while stack and height < stack[-1][0]:
                lastHeight, startIndex = stack.pop()
                area = max(area, lastHeight * (i-startIndex))
                lastIndex = startIndex
            
            stack.append([height,lastIndex])
        

        while stack:
            lastHeight, startIndex = stack.pop()
            area = max(area,lastHeight * (n-startIndex))
        
        return area
