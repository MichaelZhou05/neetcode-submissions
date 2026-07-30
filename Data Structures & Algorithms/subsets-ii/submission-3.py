class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()

        def backtrack(i , ls):
            ret.append(ls[:])
            if i >= len(nums) :
                return
            ls.append(nums[i])
            backtrack(i+1, ls)
            ls.pop()
            i -= 1
            while i+1 < len(nums) and nums[i+1] == nums[i] :
                i += 1
            i += 1
            if i < len(nums):
                ls[-1] = nums[i]
                backtrack(i+1, ls)
        
        backtrack(1, nums[:1])
        return ret
                