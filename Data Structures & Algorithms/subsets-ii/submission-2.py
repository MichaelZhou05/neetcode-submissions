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
            while i+1 < len(nums) and nums[i+1] == nums[i] :
                i += 1
            i += 1
            ls[-1] = nums[i]
            backtrack(i+1, ls)
        
        backtrack(0, [])
        return ret
                