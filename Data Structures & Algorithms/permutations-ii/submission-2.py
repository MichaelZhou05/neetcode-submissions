class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:    
        currentPerm = set()

        for i,num in enumerate(nums):
            if not len(currentPerm):
                currentPerm.add(tuple([num]))
                continue
            nextPerm = set()
            for arr in list(currentPerm):
                for j in range(len(arr)):
                    nextList = list(arr[:j]) + [num] + list(arr[j:])
                    nextPerm.add(tuple(nextList))
                nextPerm.add(tuple(list(arr) + [num]))
            currentPerm = nextPerm

        
        return list(currentPerm)

