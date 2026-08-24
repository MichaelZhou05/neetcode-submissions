class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #  total num of dom elements = k
        #  
        # [2,1,3,1,1,1,7,1,2,1]
        #    ^
        n = len(nums)
        count = Counter(nums)
        dom = None
        domCount = 0
        for key,val in count.items():
            if val > domCount:
                dom = key
                domCount = val
        
        if domCount <= n/2:             # no dominate element
            return -1
        
        leftDom = 0
        rightDom = domCount
        for i in range(n):
            if nums[i] == dom:
                leftDom += 1
                rightDom -= 1
            
            if leftDom > (i+1)/2 and rightDom > (n-(i+1))/2:
                return i
        

        return -1
        



        