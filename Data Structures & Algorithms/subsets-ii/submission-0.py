class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        def dfs(index, arr) :
            ret.append(arr[:])
            if index >= len(nums):
                return
            arr.append(nums[index])
            dfs(index +1, arr[:])
            while index+1 < len(nums) and nums[index+1] == nums[index]:
                index +=1 
            index += 1
            if index >= len(nums) :
                return
            print(nums[index])
            arr[-1] = nums[index]
            dfs(index+1, arr)
        
        dfs(0,[])
        return ret
                