class Node:
    def __init__(self,key, value, freq, next, parent):
        self.key=key
        self.value = value
        self.freq = freq
        self.next = next
        self.parent = parent


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curr = 0
        
        head = Node(-1,-1,-1,None,None)
        tail = Node(-1,-1,-1,None,None)
        head.next = tail
        tail.parent = head
        self.bucket = [[head,tail]]    #index = used count --> linked list (head, tail)
        # head --> node --> node --> tail
        #           ^LRU
        self.hashmap = {}   #key --> node

        self.LFU = None

    def get(self, key: int) -> int:
        if key not in self.hashmap : return -1
        node = self.hashmap[key]

        #remove node from current bucket
        node.next.parent = node.parent
        node.parent.next = node.next

        #next bucket
        node.freq += 1
        if node.freq-1 == len(self.bucket):
            head = Node(-1,-1,-1,None,None)
            tail = Node(-1,-1,-1,None,None)
            head.next = tail
            tail.parent = head
            self.bucket.append([head,tail])

        head,tail = self.bucket[node.freq-1]

        #insert node at lend of LRU list
        tail.parent.next = node
        node.parent = tail.parent
        node.next = tail
        tail.parent = node

        #update LFU
        head,tail = self.bucket[self.LFU-1]
        if head.next is tail: #bucket is empty
            self.LFU += 1
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.get(key)
            return
        
        #inseart new
        if self.curr < self.cap: 
            self.curr+=1
        else: #evict
            node = self.bucket[self.LFU-1][0].next
            del self.hashmap[node.key]
            node.next.parent = node.parent
            node.parent.next = node.next


        #acutally insert new
        node = Node(key,value,1,None,None)
        head,tail = self.bucket[node.freq-1]
        
        #insert node at end of LRU
        tail.parent.next = node
        node.parent = tail.parent
        node.next = tail
        tail.parent = node

        self.LFU = 1
        self.hashmap[key] = node



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# currCap = curr num of elements in cache
# evict only happens
# put --> key not in cache, and cap full 