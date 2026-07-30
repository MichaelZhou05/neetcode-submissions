class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {} #value -> count

        for val in nums :
            counter[val] = counter.get(val,0) + 1
        
        print(counter)
        arr = [[]] * len(nums)

        for val in counter :
            arr[counter[val]].append(val)
            print(arr)

        return  arr



            
