class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = set()
        s.add(0)
        s.add(nums[0])

        target = sum(nums)/2

        for i in range(1,len(nums),1):
            ls1 = list(s)
            for num in ls1:
                val = num+nums[i]
                if val == target:
                    return True
                s.add(num+nums[i])
        
        return False
        