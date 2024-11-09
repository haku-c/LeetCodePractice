class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        opt = [0] * len(values)
        currentMax = values[0]
        opt[0] = 0
        for i in range(1, len(values)):
            currentMax = currentMax - 1
            opt[i] = values[i] + currentMax
            currentMax = max(currentMax, values[i])
        return max(opt)
