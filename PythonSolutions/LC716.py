from sortedcontainers import SortedList


# as others have mentioned, we can get O(1) insert and removal with the double link list similar to LRU Cache
# this solution is double linked list with tree map approach
class Node:
    def __init__(self, x):
        self.next = None
        self.prev = None
        self.val = x


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node: Node):
        last = self.tail.prev
        last.next = node
        node.next = self.tail
        node.prev = last
        self.tail.prev = node

    def remove(self, node: Node):
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous


class MaxStack:
    # double - link list to track the stack
    # heap to track max elements. The heap stores nodes at the requisite values
    # allows for restitching of nodes if we remove using popmax

    def __init__(self):
        self.stack = DoubleLinkedList()
        self.order = SortedDict()

    def push(self, x: int) -> None:
        node = Node(x)
        self.stack.append(node)
        lst = self.order.get(x, [])
        lst.append(node)
        self.order[x] = lst
        # print(self.top())

    def pop(self) -> int:
        node = self.stack.tail.prev
        self.stack.remove(node)
        self.order.get(node.val).pop()
        if len(self.order.get(node.val)) == 0:
            del self.order[node.val]
        return node.val

    def top(self) -> int:
        return self.stack.tail.prev.val

    def peekMax(self) -> int:
        return self.order.peekitem()[0]

    def popMax(self) -> int:
        nodeList = self.order.peekitem()[1]
        node = nodeList.pop()
        self.stack.remove(node)
        if len(nodeList) == 0:
            del self.order[node.val]
        return node.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# cheated a bit using sortedDictionary (with list in case you have duplicated values).

# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

# Implement the MaxStack class:

#     MaxStack() Initializes the stack object.
#     void push(int x) Pushes element x onto the stack.
#     int pop() Removes the element on top of the stack and returns it.
#     int top() Gets the element on the top of the stack without removing it.
#     int peekMax() Retrieves the maximum element in the stack without removing it.
#     int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

# You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.

# I also want to state the first editorial solution leverages sortedContainers, which is optimistic for an interview setting.

# here's a solution i like better: track what's removed in a separate set (O(1) amortized) and if the value is removed, disregard
import heapq


class MaxStack:

    def __init__(self):
        self.heap = []
        self.cnt = 0
        self.stack = []
        self.removed = set()

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        num, idx = heapq.heappop(self.heap)
        self.removed.add(-idx)
        return -num


# this way we can leverage a heap (which is natural for min and max problems). Don't forget to make a max heap
