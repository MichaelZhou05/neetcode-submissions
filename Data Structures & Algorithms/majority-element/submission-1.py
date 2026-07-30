class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currMaj = nums[0]
        currCount = 0

        for num in nums:
            if currMaj == num:
                currCount += 1
                continue
            else:
                if currCount == 0:
                    currMaj = num
                    currCount += 1
                else:
                    currCount -= 1
        

        return currMaj
