class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} #value -> count

        for val in nums :
            counter[val] = counter.get(val,0) + 1
        
        arr = [[] for i in range(len(nums) + 1)]

        for val in counter :
            ct = counter[val]
            arr[ct].append(val)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res





            
