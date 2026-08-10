class StockSpanner:

    def __init__(self):
       self.history = [[float('inf'),1]]

    def next(self, price: int) -> int:
        span = 1
        while price >= self.history[-1][0]:
            val, newSpan = self.history.pop()
            span += newSpan
        
        self.history.append([price,span])
        return span

        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)