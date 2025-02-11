from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.indices = defaultdict(list)
        self.container = {}

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.indices[number], index)
        self.container[index] = number

    def find(self, number: int) -> int:
        # remove from the heap if that index has a changed value since it was added to this heap
        while (
            self.indices[number] and self.container[self.indices[number][0]] != number
        ):
            heapq.heappop(self.indices[number])
        if self.indices[number] == []:
            return -1
        return self.indices[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# the only trick is to make sure you use heappops to get logn time on removals
# i originally use a list remove which is O(n)
