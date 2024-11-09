class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        sum = 0
        window = 0
        for i in range(minutes):
            if grumpy[i] == 0:
                sum += customers[i]
            if grumpy[i] == 1:
                window += customers[i]
        max = window
        for i in range(minutes, len(customers)):
            if grumpy[i] == 0:
                sum += customers[i]
            if grumpy[i - minutes] == 1:
                window -= customers[i - minutes]
            if grumpy[i] == 1:
                window += customers[i]
            if window > max:
                max = window
        return max + sum


# you can do this question in one pass. The idea is you want to flip the most minutes to get the largest gain.
# you can use a sliding window to get
