class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.lruCache = {}
        self.store = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next, self.right.prev = self.right, self.left

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insertNode(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.lruCache:
            self.removeNode(self.lruCache[key])
            self.insertNode(self.lruCache[key])
            return self.lruCache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lruCache:
            self.removeNode(self.lruCache[key])
        self.lruCache[key] = Node(key, value)
        self.insertNode(self.lruCache[key])

        if len(self.lruCache) > self.store:
            lru = self.left.next
            self.removeNode(lru)
            del self.lruCache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)