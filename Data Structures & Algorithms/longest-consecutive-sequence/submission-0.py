class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = sorted(nums)
        count = 1
        init = ls[0]
        for num in ls:
            if num == init + 1 : 
                count += 1
                init = num
            elif (num > init + 1) :
                return count
        return count