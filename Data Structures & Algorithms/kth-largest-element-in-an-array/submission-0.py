class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums 
        heapq.heapify(heap)

        ls = heapq.nlargest(k, heap)
        return ls[-1]