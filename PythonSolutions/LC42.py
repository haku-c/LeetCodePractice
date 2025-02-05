from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        queue = deque()
        n = len(height)
        res = 0
        waterLevel = 0
        for i in range(n):
            currentHeight = height[i]
            while queue:
                if queue[-1][0] < currentHeight:
                    lastHeight, lastIndex = queue.pop()
                    res += (i - lastIndex - 1) * (lastHeight - waterLevel)
                    waterLevel = lastHeight
                else:
                    res += (i - queue[-1][1] - 1) * (currentHeight - waterLevel)
                    waterLevel = currentHeight
                    break
            queue.append((currentHeight, i))
            waterLevel = currentHeight
        return res


# the idea is we want to keep the height values in the queue to be decreasing
# if we encounter a boundary that is greater than the past entries, then we should REMOVE values from the queue.
# this is because anything smaller than this maximal height on the left cannot trap more water with things on the right of this boundary
# ex/ 19, 12, 20, 33, 24: when we get to the 20, it's impossible for the 19 or 12 to ever trap water with 33 or 24

# so we have two cases:
# if the most recent height was less than the current, we need to remove that recent height and trap all water between that index
# and the current one. This is done by setting all the heights in between i and lastindex to be the current waterlevel
# then we set the new water level to be the level at lastIndex

# note how this handles edge cases: if the boundaries are adjacent, there are no squares to trap between, so res does not increment
# (i - lastIndex - 1) = 0
# similarly, if there are 2 boundaries of the same height in a row, then the waterLevel remains the same, so lastHeight - waterLevel = 0

# if the last entry is taller than the current boundary, we dont want to remove it from the queue. However, we still may
# need to adjust the waterLevel depending on the values. Since the currentHeight is the lower boundary, we set all the
# open cells to currentHeight. Then the current waterLevel is currentHeight
# break from the loop

# append the newest height and index, and make sure the new current waterLevel is updated
