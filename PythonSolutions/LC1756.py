class MRUQueue:

    def __init__(self, n: int):
        self.queue = SortedSet([(i, i) for i in range(1, n + 1)])

    def fetch(self, k: int) -> int:
        _, val = self.queue[k - 1]
        del self.queue[k - 1]
        if len(self.queue) > 0:
            highest = self.queue[-1][0]
        else:
            highest = 0
        self.queue.add((highest + 1, val))
        return val


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

# my version is sorted list which uses sortedcontainers.
# other approaches are linkedlist (O(n) fetch)
# and segment tree a segment tree is useful here because we can see that the input space is a small consecutive range

# Design a queue-like data structure that moves the most recently used element to the end of the queue.

# Implement the MRUQueue class:

#     MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
#     int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.

# ex/
# Input:
# ["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
# [[8], [3], [5], [2], [8]]
# Output:
# [null, 3, 6, 2, 2]
