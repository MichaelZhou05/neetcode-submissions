class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = numbers.index(target) - 1

        while l < r and not numbers[l] + numbers[r] == target:
            if numbers[l] + numbers[r] > target :
                r -= 1
            elif numbers[l] + numbers[r] < target :
                l += 1
        
        return [l+1, r+1]
            
