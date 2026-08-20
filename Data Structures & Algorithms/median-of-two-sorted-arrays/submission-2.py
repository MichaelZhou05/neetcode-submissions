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
        #x= 0
        #y= 1
        n = len(nums1) + len(nums2)

        l,r = 0, min(n//2, len(nums1))

        while l<r:
            x = (l+r)//2
            y = (n//2)-x

            if nums1[x] < nums2[y-1]:
                l = x+1
            elif nums1[x-1] > nums2[y]:
                r = x-1
            else: 
                l,r = x,x


        if n%2: #odd
            return float(nums1[l]) if l<len(nums1) else float(nums2[l-len(nums1)])
        else:
            first = float(nums1[l]) if l<len(nums1) else float(nums2[l-len(nums1)])
            second = float(nums1[l+1]) if l+1<len(nums1) else float(nums2[l+1-len(nums1)])
            return (first + second)/2
