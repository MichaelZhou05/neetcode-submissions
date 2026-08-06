class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return False 
        
        l,r = 0,0
        contains = set()
        while r-l < k:
            contains.add(nums[r])
            r+=1
        
        while r<len(nums):
            if len(contains) < k+1:
                return True
            contains.remove(nums[l])
            l+= 1
            contains.add(nums[r])
            r+=1
        

        return len(contains) < k+1