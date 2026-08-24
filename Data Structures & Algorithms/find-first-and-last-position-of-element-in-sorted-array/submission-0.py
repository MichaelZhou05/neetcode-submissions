class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #find left
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
        
        ret.append(r)

        #find right
        l,r = 0,len(nums)-1
        while l<r:
            print(l,r)
            mid = (l+r)//2+1
            if nums[mid]<target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                l=mid
        
        ret.append(l)
        return ret