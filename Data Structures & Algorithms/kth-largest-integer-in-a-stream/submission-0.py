import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.heap1 = nums 
        heapq.heapify(self.heap1)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap1, val)
        ls1 = heapq.nlargest(self.k, self.heap1)
        return ls1[-1]


