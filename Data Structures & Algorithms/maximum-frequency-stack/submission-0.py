class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.hq = []    #[-count, -index, value]
        self.index = 0


    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush(self.hq, [-1*self.count[val],-1*self.index,val])  
        self.index += 1

    def pop(self) -> int:
        #most frequent element (right most occurence)
        arr = heapq.heappop(self.hq)
        val = arr[2]
        self.count[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()