class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        print(nums)
        

        for i, n in enumerate(nums) :
            if i > 0 and nums[i] == nums [i-1] : 
                continue

            target = -1*n
            
            l = i+1
            r = len(nums) - 1
            while l < r :
                if nums[l] + nums[r] > target : r -= 1
                elif nums[l] + nums[r] < target : l += 1
                else : 
                    ret.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    
        return ret
