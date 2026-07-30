class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0, k-1
        localMax =[nums[l],0] #[max, relative postition]

        for i in range(l+1,r+1) :
            if nums[i] > localMax[0] :
                localMax = [nums[i], i-l]

        output = [localMax[0]]

        r+=1
        l+=1
        localMax[1] -= 1

        while r < len(nums) :
            if localMax[1] >= 0 :
                if localMax[0] > nums[r] : 
                    output.append(localMax[0])
                else:
                    output.append(nums[r]) 
                    localMax = [nums[r], r-l]
            else :
                localMax = [nums[l],l]

                for i in range(l+1,r+1) :
                    if nums[i] > localMax[0] :
                        localMax = [nums[i], i-l]
                output.append(localMax[0])
            
            r+=1
            l+=1
            localMax[1] -= 1

        return output                
            