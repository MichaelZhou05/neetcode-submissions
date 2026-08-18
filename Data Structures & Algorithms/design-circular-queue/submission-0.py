class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.currSize = 0
        self.que = [None for _ in range(k)]
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.currSize == self.cap : return False
        
        self.rear = (self.rear + 1) % self.cap
        self.que[self.rear] = value
        self.currSize += 1
        return True

    def deQueue(self) -> bool:
        if self.currSize == 0 : return False

        self.currSize -= 1
        self.que[self.front] = None
        self.front = (self.front + 1) % self.cap
        return True        	

    def Front(self) -> int:
        if self.currSize:
            return self.que[self.front]
        return -1

    def Rear(self) -> int:
        if self.currSize: return self.que[self.rear]
        return -1


    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
       	return self.cap == self.currSize
