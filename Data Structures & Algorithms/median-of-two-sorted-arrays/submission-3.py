class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #by def
        # medium  means # of elements < is = n//2

        # (x+1)+ (y+1) = n//2

        
        # v  
        #[1,2]
        #[3,4]
        # ^
        #l = 2
        #r = 2
        #x= 1
        #y= 1

        #   
        #[1,3]
        #[2]
        # ^
        #l = 1
        #r = 1
        #x= 1
        #y= 1
        n = len(nums1) + len(nums2)

        l,r = 0, min(n//2, len(nums1))

        while l<r:
            x = (l+r)//2
            y = (n//2)-x

            if y>0 and nums1[x] < nums2[y-1]:
                l = x+1
            elif x>0 and nums1[x-1] > nums2[y]:
                r = x-1
            else: 
                l,r = x,x

        x = l
        y = (n//2) - x


        if n%2: #odd
            return min(nums1[x] if x<len(nums1) else float('inf'), nums2[y] if y<len(nums2) else float('inf'))
        else:
            second = min(nums1[x] if x<len(nums1) else float('inf'), nums2[y] if y<len(nums2) else float('inf'))
            first = max(nums1[x-1] if x>0 else float('inf'), nums2[y-1] if y>0 else float('inf'))
            return (first+second)/2