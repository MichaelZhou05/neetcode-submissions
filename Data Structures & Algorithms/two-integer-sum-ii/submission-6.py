class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        
        close = target
        while close not in numbers :
            close -= 1
        
        r = numbers.index(close) -1
        print(l)
        print(r)

        while l < r :
            if numbers[l] + numbers[r] == target :
                return [l+1, r+1]
            if numbers[l] + numbers[r] > target :
                r -= 1
            elif numbers[l] + numbers[r] < target :
                l += 1
        
        return [l+1, r+1]