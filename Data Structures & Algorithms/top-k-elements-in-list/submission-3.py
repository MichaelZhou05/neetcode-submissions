class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} #value -> count

        for val in nums :
            counter[val] = counter.get(val,0) + 1
        
        print(counter)
        arr = [[] for i in range(len(nums) + 1)]

        for val in counter :
            ct = counter[val]
            arr[ct].append(val)

        return  arr



            
