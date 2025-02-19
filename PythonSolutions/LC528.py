import random


class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        cumSum = sum(w)
        probWeights = list(map(lambda x: x / cumSum, w))
        self.values = [0] * self.n
        self.values[0] = probWeights[0]
        for i in range(1, self.n):
            self.values[i] = self.values[i - 1] + probWeights[i]

    def pickIndex(self) -> int:
        chosenPercent = random.uniform(0, 1)
        start = 0
        end = self.n - 1
        while start <= end:
            middle = start + (end - start) // 2
            if self.values[middle] > chosenPercent:
                end = middle - 1
            else:
                start = middle + 1
        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# we want to get a prefix sum of the percentages
# this is because we need to find the range corresponding to each integer in our range
# so if there is a 25% chance assigned to 0 and a 50% percent change assigned to 1 and a 25% chance assigned to 2
# then we assigned 0 - .25 to 0, .25 - .75 to 1, .75 - 1 to 2
# then we uniformly sample from 0 to 1 and see which range our value is in
