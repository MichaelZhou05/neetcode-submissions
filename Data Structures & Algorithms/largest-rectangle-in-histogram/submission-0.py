class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = max(heights)



        # 3,5,7,4

        [7,2]
        [5,1]
        [3,0]
        for i,height in enumerate(heights):
            if not stack or height > stack[-1][0]:
                stack.append([height,i])
                continue
            
            lastIndex = 0
            while height < stack[-1][0]:
                lastHeight, startIndex = stack.pop()
                area = max(area, lastHeight * (i-startIndex))
                lastIndex = startIndex
            
            stack.append([height,lastIndex])
        

        while stack:
            area = max(area,)
