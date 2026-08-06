class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=nums[0]
        rotate = None
        for i,val in enumerate(nums):
            if val < l:
                rotate = i
                break
            l=val
        
        l,r = rotate, rotate-1+len(nums)
        # 0 1 2 3 4 5 6 7| 8 9 10 11 12
        # 3 4 4 5 6 1 2 2| 3 4 4  5  6
        # 1 2 2 3 4 4 5 6

        #0,1,2,3,4,5,6
        #3,5,6,0,0,1,2
        #0,0,1,2,3,5,6


        #mapped r index  = r%len(nums)
        #mapped mid = (r+l)/2%len(nums)
        mid = None
        while l<=r :
            print(l)
            print(r)
            mid = (r+l)//2
            print(mid)
            if target < nums[mid%len(nums)]:
                r = mid-1
            elif target > nums[mid%len(nums)]:
                l = mid+1
            else:
                return True
        
        return False


            
