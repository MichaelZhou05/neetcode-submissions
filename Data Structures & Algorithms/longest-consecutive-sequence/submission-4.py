class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ls = sorted(nums)
        print(ls)
        init = ls[0]
        
        countMax = 0
        count = 1

        for num in ls:
            if num == init + 1 : 
                count += 1
                init = num
            elif (num > init + 1) :
                 countMax = max(countMax, count)
                 count = 1
                 init = num
        countMax = max(count, countMax)
        return countMax