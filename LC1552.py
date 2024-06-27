class Solution(object):

    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        # def getCloser(target, val1, val2):
        #     if target - val1 >= val2 - target:
        #         return val2
        #     else:
        #         return val1

        # def binarySearch(position, start, end, target):
        #     if target <= position[start]:
        #         return position[start]
        #     if target >= position[end]:
        #         return position[end]
        #     while start < end:
        #         current = start + (end - start) / 2
        #         if position[current] == target:
        #             return target
        #         elif position[current] > target:
        #             # check to see if the current value is closer than the adjacent one
        #             if current > 0 and target > position[current - 1]:
        #                 return getCloser(
        #                     target, position[current - 1], position[current]
        #                 )
        #             end = current
        #         else:
        #             if current < len(position) - 1 and target < position[current + 1]:
        #                 return getCloser(
        #                     target, position[current], position[current + 1]
        #                 )
        #             start = current + 1
        #     return position[current]

        # we can check if this interval size will work by just greedily constructing the intervals if the condition is satisfied
        def check(positions, interval, numBalls):
            current = 0
            numBalls = numBalls - 1
            for i in range(1, len(positions)):
                if positions[i] - positions[current] >= interval:
                    current = i
                    numBalls -= 1
            return numBalls <= 0

        position.sort()
        res = -1
        startInterval = 1
        endInterval = (position[len(position) - 1] - position[0]) // (m - 1) + 1
        while startInterval <= endInterval:
            currentInterval = startInterval + (endInterval - startInterval) // 2
            if check(position, currentInterval, m):
                res = currentInterval
                startInterval = currentInterval + 1
            else:
                endInterval = currentInterval - 1
        return res
