class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s1 = set(nums)
        
        counter = 1
        countMax = 0

        while len(s1) > 0 :
            smallest = min(s1)
            s1.remove(smallest)
            print("break")
            print(smallest)
            counter = 1

            while smallest + 1 in s1 :
                counter += 1
                smallest += 1
                s1.remove(smallest)
            countMax = max(countMax, counter)
            

        return countMax

