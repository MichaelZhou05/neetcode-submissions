class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # 1 3 -1 -3 5 3 6 7
        #             ^    ^
        # out : 3,3,5,5,6
        # max  7
        # for each element pop checked if it is the max, if so pop from max deque
        # check if new incoming element > curr max if so repalce

        maxDeque = deque([nums[0]])
        for i in range(1,k):
            while len(maxDeque) and nums[i] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[i])
        
        ret = [maxDeque[0]]
        for i in range(len(nums)-k):
            if nums[i] == maxDeque[0]:
                maxDeque.popleft()
            while len(maxDeque) and nums[i+k] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[i+k])
            ret.append(maxDeque[0])
        
        return ret