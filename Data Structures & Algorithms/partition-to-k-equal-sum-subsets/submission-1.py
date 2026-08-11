class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total =  sum(nums)
        target = total/k
        if float.is_integer(target):
            target = int(target)
        else:
            return False


        def backtrack(currIndex, currTarget, used, k):
            if k == 0:
                return True

            if currTarget == 0:
                nonlocal target
                return backtrack(0, target, used, k-1)   

            if currIndex >= len(nums) or currTarget < 0:
                return False


            if currIndex in used:
                return backtrack(currIndex+1, currTarget, used,k)

            unUse = backtrack(currIndex+1,currTarget,used,k)
            if unUse: return True
            used.add(currIndex)
            use = backtrack(currIndex+1, currTarget-nums[currIndex],used,k)
            used.remove(currIndex)
            return use or unUse
        
        return backtrack(0,target, set(),k)
            

