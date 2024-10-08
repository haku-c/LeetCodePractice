from collections import Counter
import random


# the objective is to find the minimum amount of boxes you need to get rid of such that of the remaining boxes, max(boxes) <= min(boxes) * capacity
# the approach is to try every possible pair of minimum and maximum box counts and find the best result.
# if we store the counts, we can have every loop iteration be a constant amount of work.
# time complexity is nlogn + n^2 + n
# the Counter is O(n)
# the sort is nlogn
# testing every pair is O(n^2)


class Solution:
    def box(self, sizes, capacity):
        c = Counter(sizes)
        totalBoxCount = 0
        cummulativeCounts = {}
        for size in sorted(c):
            totalBoxCount += c[size]
            cummulativeCounts[size] = totalBoxCount
        sortedBoxes = sorted(set(sizes))

        res = float("inf")
        for lower in range(len(sortedBoxes)):
            for upper in range(lower + 1, len(sortedBoxes)):
                minimum = sortedBoxes[lower]
                maximum = sortedBoxes[upper]
                if minimum * capacity >= maximum:
                    res = min(
                        res,
                        cummulativeCounts[minimum]
                        - c[minimum]
                        + (len(sizes) - cummulativeCounts[maximum]),
                    )
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.box([2, 3, 2, 2, 1, 3], 2))
    print(test.box([2, 3, 2, 2, 1, 3, 11], 3))
    print(test.box([3, 3, 3, 4, 5, 7, 7, 8], 2))
    lst = []
    for i in range(10**7):
        lst.append(random.randint(1, 100))
    print(test.box(lst, 8))
