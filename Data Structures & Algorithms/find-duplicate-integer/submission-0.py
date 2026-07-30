class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = max(nums)
        count = n*(n+1) // 2

        total = 0
        for i in nums :
            total += i
        
        print(total)
        print(count)
        print
        return (total-count)//(len(nums)-n)