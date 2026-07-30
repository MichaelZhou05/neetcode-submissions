class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Rob houses [0...n-2]
        arr1 = nums[:-1]
        dp1 = [0] * (len(arr1) + 1)
        for i in range(2, len(arr1) + 1):
            dp1[i] = max(arr1[i - 2] + dp1[i - 2], dp1[i - 1])

        # Rob houses [1...n-1]
        arr2 = nums[1:]
        dp2 = [0] * (len(arr2) + 1)
        for i in range(2, len(arr2) + 1):
            dp2[i] = max(arr2[i - 2] + dp2[i - 2], dp2[i - 1])

        return max(dp1[-1], dp2[-1])