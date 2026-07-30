class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate values for i

            l, r = i + 1, len(nums) - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates for l and r
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return ret