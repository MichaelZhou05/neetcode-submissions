class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} #value -> count

        for val in nums :
            counter[val] = counter.get(val,0) + 1
        
        inv_map = {v: k for k, v in counter.items()} # count -> value
        ret =[]
        for i in range(k) :
            maxCount = max(inv_map)
            maxVal = inv_map[maxCount]
            print(maxVal, ' : ' , maxCount)
            ret.append(maxVal)
            inv_map.pop(maxCount)
        
        return ret



            
