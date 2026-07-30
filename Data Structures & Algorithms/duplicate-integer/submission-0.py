class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for num in nums :
            hs.add(num)
        return len(hs) != len(nums)


         