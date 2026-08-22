class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = deque([[nums[0],0]])
        n = len(nums)

        for i in range(1,k):
            while maxElements and nums[i] > maxElements[-1][0]:
                maxElements.pop()
            maxElements.append([nums[i],i])
        
        ret = [maxElements[0][0]]

        for start in range(1,n-k+1):
            while start > maxElements[0][1]:
                maxElements.popleft()
            end = start+k-1
            while maxElements and nums[end] > maxElements[-1][0]:
                maxElements.pop()
            maxElements.append([nums[end],end])

            ret.append(maxElements[0][0])
        
        return ret