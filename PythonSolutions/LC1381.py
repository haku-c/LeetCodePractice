class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        end = min(k, len(self.stack))
        for i in range(end):
            self.stack[i] += val


# a really cool solution involves tracking the increments in a separate array (so doubles the space potentially)
# however, this reduces the need to do an O(k) operation at every increment
# you can store the increment and apply it on a pop operation if an increment reached that index.
