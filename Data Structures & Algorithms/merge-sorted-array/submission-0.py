class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        ret = []
        while i<m and j<n:
            print(i,j)
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        print(ret)
        if j < n:
            ret = ret + nums2[j:n]
        if i < m:
            ret = ret + nums1[i:m]
        
        nums1[:] = ret