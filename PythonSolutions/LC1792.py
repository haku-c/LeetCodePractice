import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratios = [(-((x + 1) / (y + 1) - x / y), x, y) for x, y in classes]
        heapq.heapify(ratios)
        while extraStudents > 0:
            _, passingStudents, totalStudents = heapq.heappop(ratios)
            add = (
                -(
                    ((passingStudents + 2) / (totalStudents + 2))
                    - (passingStudents + 1) / (totalStudents + 1)
                ),
                passingStudents + 1,
                totalStudents + 1,
            )
            heapq.heappush(ratios, add)
            extraStudents -= 1
        s = sum(a / b for _, a, b in ratios) / len(classes)
        return s


# good practice on list comprehensions and using a heap.
# my original reasoning was wrong, you need to explicitly calculate what gives you the biggest increase in ratio
