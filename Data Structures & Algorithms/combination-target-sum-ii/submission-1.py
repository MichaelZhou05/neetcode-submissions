class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(val, index, ls) :
            if val == target and ls not in ret:
                ret.append(ls)
                return

                        
            while index < len(nums) :
                print(index)
                if val + nums[index] > target : 
                    index += 1
                    continue
                newVal = val + nums[index]
                ls.append(nums[index])
                dfs(newVal, index + 1, ls.copy())
                ls.pop()
                index += 1
        

        dfs(0, 0, [])
        return ret
            
