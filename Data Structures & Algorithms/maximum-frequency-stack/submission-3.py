class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.stacks = [None]
        self.currMaxCount = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] > self.currMaxCount:
            self.stacks.append([])
            self.currMaxCount += 1
        
        self.stacks[self.count[val]].append(val)


    def pop(self) -> int:
        ret = self.stacks[self.currMaxCount].pop()
        self.count[ret] -= 1
        if len(self.stacks[self.currMaxCount]) == 0:
            self.stacks.pop()
            self.currMaxCount -= 1
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()