class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.last = LinkedListNode(-1,-1)
        self.first = LinkedListNode(-1,-1)
        self.last.prev = self.first
        self.first.next = self.last

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # add pushes the node specified to the front of the linked list
    def add(self, node):
        temp = self.first.next
        self.first.next = node
        node.prev = self.first
        node.next = temp
        temp.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            tempNode = self.cache[key]
            self.delete(tempNode)
            self.add(tempNode)
            self.cache[key] = self.first.next
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if we are only updating the value of an existing key, we need to move the current order of that 
        # key in the linked list and 
        if key in self.cache:
            temp = self.cache[key]
            self.delete(temp)
            temp.val = value
        elif len(self.cache) == self.capacity:
            # toRemove is the LRU key. delete the node from the tracking list and the cache
            toRemove = self.last.prev
            self.delete(toRemove)
            del self.cache[toRemove.key]
            # create a new node and add this at the front (most recently used)
            temp = LinkedListNode(key, value)
        else:
            # otherwise we don't have to remove anything and can just add to the cache and the linked list
            temp = LinkedListNode(key, value)
        self.add(temp)
        self.cache[key] = self.first.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)