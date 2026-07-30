class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fin = {0 : 0 *k } # value -> count
        counter = defultdic(int)
        for val in nums :
            counter[val] = counter.get(val,0) + 1
            if counter[val] > min(fin.values()) : 
                return

            
