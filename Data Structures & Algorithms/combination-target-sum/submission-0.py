class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()

        def dfs(val, index, ls) :
            if val > target : 
                return
            if val == target:
                ret.append(ls)
                return
            
            while index < len(nums) :
                newVal = val + nums[index]
                ls.append(nums[index])
                dfs(newVal, index, ls.copy())
                ls.pop()
                index += 1
        

        dfs(0, 0, [])
        return ret
            
