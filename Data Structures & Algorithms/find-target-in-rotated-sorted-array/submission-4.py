class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r : 
            mid = (l+r)//2

            if nums[mid] == target: 
                return mid
            elif target < nums[mid] :
                if target > nums[l] :
                    r = mid
                else: 
                    l = mid
            else:
                if target < nums[r] :
                    l = mid
                else: 
                    r = mid


        return -1