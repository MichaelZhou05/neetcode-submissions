class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total =  sum(nums)
        target = total/k
        if float.is_integer(target):
            target = int(target)
        else:
            return False

        used = set()

        def backtrack(currIndex, currTarget, k):
            if k == 0:
                return True

            if currTarget == 0:
                nonlocal target
                return backtrack(0, target, k-1)   

            if currIndex >= len(nums) or currTarget < 0:
                return False

            if currIndex in used:
                return backtrack(currIndex+1, currTarget, k)
            
            used.add(currIndex)
            if currTarget-nums[currIndex] >= 0 and backtrack(currIndex+1, currTarget-nums[currIndex], k):
                return True
            used.remove(currIndex)
            return backtrack(currIndex+1, currTarget, k)
        
        return backtrack(0,target,k)
            

