class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if n > m:
            m, n = n, m

        l,r = 0, n-1
        half = (m+n)//2

        mid = 0
        part = 0

        while l<=r : 
            mid = (l+r)//2
            part = half - mid - 2
            if nums1[mid] <= nums2[part+1] and nums2[part] <= nums1[mid+1] :
                break
            elif nums1[mid] > nums2[part+1] :
                r = mid -1
            else :
                l = mid +1


        if (m+n)%2 != 0:
            return min(nums1[mid+1], nums2[part+1])
        else:
            return (max(nums1[mid], nums2[part]) + min(nums1[mid+1], nums2[part+1])) / 2






