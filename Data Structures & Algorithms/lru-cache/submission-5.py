class Node:
    def __init__(self, key, val, prev, nxt):
        self.val, self.key = val ,key
        self.prev, self.next = prev, nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.mp1 = {}  #key -> node
        self.head = self.tail = None
        

    def get(self, key: int) -> int:
        if key in self.mp1 :
            self.moveNode(self.mp1[key])
            return self.mp1[key].val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.mp1:
                self.mp1[key].val = value
                self.moveNode(self.mp1[key])
        else: 
            if self.count < self.capacity :
                self.count+= 1
            else:
                del self.mp1[self.tail.key]
                if self.tail.prev:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev

            
            self.head = self.mp1[key] = Node(key, value, self.head, None)
            if not self.tail: 
                self.tail = self.head
            

        
    def moveNode(self, node):
        if node == self.head:
            return

        # Remove node from its current spot
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            # It was tail
            self.tail = node.prev

        # Insert node at front
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node



