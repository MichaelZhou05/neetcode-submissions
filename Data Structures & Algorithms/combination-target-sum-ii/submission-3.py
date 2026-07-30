class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()

        def dfs(val, index, ls) :
            if val == target:
                ret.append(ls)
                return

                        
            while index < len(nums) :
                if val + nums[index] > target : 
                    index += 1
                    continue
                newVal = val + nums[index]
                ls.append(nums[index])
                dfs(newVal, index + 1, ls.copy())
                ls.pop()
                while index + 1 < len(nums) and nums[index+1] == nums[index]: 
                    index +=1
                index += 1
        

        dfs(0, 0, [])
        return ret
            
