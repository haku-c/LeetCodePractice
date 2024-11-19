class LinkedListNode:
    def __init__(self, b=None, m=None, v=0):
        self.before = b
        self.currentMin = m
        self.val = v


class MinStack:

    def __init__(self):
        self.topNode = None

    def push(self, val: int) -> None:
        if self.topNode is None:
            self.topNode = LinkedListNode(None, val, val)
        else:
            self.topNode = LinkedListNode(
                self.topNode, min(self.topNode.currentMin, val), val
            )

    def pop(self) -> None:
        self.topNode = self.topNode.before

    def top(self) -> int:
        return self.topNode.val

    def getMin(self) -> int:
        return self.topNode.currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# you just need to track the minimum value at the point of insertion of each value into the stack
# you can also have 2 separate lists, one to track the stack (append to end in constant time) and the other to track the mins
