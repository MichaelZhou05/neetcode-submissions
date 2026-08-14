class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        occur = [[] for _ in range(len(nums)+1)]
        for num, occurances in count.items():
            occur[occurances].append(num)
        
        ret = []
        i = len(nums)
        while len(ret) < k:
            if len(occur[i]):
                ret += occur[i]
            i-=1
        
        return ret