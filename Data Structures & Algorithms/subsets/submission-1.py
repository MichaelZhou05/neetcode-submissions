class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        def backtrack(i , ls):
            ret.append(ls[:])
            if i >= len(nums) :
                return
            ls.append(nums[i])
            backtrack(i+1, ls)
            ls.pop()
            ls[-1] = nums[i]
            backtrack(i+1, ls)
        
        backtrack(1, nums[:1])
        return ret