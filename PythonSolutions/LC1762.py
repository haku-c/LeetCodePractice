class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = deque([n - 1])
        for i in range(n - 2, -1, -1):
            if heights[i] > heights[res[0]]:
                res.appendleft(i)
        return list(res)


# this is the straightforward approach

# a more algorithmic answer is to use a stack


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        for current in range(n):
            # If the current building is taller,
            # it will block the shorter building's ocean view to its left.
            # So we pop all the shorter buildings that have been added before.
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)

        return answer


# we want a monotonic decreasing stack. Go left to right
# Remove all the entries to the left of the current entry if they have a lower height than current
# this is the solution if you need to process from left to right (say in a stream)
