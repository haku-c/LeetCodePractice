from heapq import *


class MedianFinder:
    # upper contains the upper half of the numbers in the median list, while lower contains the lower half.
    # len(upper) + 1 == len(lower) or len(upper) == len(lower), i.e length of upper differs from lower by at most 1 and upper never has less elements than lower
    def __init__(self):
        self.lower = []
        self.upper = []

    # because heaps in python always return the minimum value in the heap, we can use it as is for upper, but we want the biggest element in lower so
    # we would need to invert the heap by using negatives.
    def addNum(self, num: int) -> None:
        if len(self.lower) == len(self.upper):
            n = heappushpop(self.lower, -num)
            heappush(self.upper, -n)
        else:
            n = heappushpop(self.upper, num)
            heappush(self.lower, -n)

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (-(self.lower[0]) + self.upper[0]) / 2.0
        else:
            return float(self.upper[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# we can find the median quickly by just taking the desired operation using the two middlemost elements, which happen to be poppable from our heaps
# when we update the heaps, we need to maintain the sizes (so that in the odd length case of findMedian the median is the smallest element in upper)
# consider the cases:
# lower  upper
# 12     34    add 0. -> 01 234 is the desired output. To achieve this, we need to shift one element from lower to upper. (in this case, the biggest one in lower)
# this means we should first add the desired number (0 here) and then get the biggest element from lower and push that onto upper
#
# conversely
# 1     34    add 0. -> 01 34 is the desired output. We need to make sure to push a value onto the lower heap.
# first push a value onto upper, find the minimum after that add and push that popped value onto lower.
