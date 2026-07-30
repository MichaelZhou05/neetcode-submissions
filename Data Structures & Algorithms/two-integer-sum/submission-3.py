class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flip = {}
        for i in range(len(nums)) :
            flip[nums[i]] = i
        for val in nums :
            if flip.get(target-val, -1) != -1 :
                first = flip.get(val)
                flip.pop(val)
                return [first ,flip.get(target-val)]


