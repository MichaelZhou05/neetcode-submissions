class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #find left
        if not nums:
            return [-1,-1]
        ret =[]
        l,r = 0,len(nums)-1
        while l<r:
            print(l,r)
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                r=mid
        
        ret.append(r if r >=0 and  nums[r] == target else -1)

        #find right
        l,r = 0,len(nums)-1
        while l<r:
            print(l,r)
            mid = math.ceil((l+r)/2)
            if nums[mid]<target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                l=mid
        
        ret.append(l if l < len(nums) and nums[l] == target else -1)
        return ret