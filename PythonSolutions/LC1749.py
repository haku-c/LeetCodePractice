class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currentMax = 0
        currentMin = 0
        res = 0
        for n in nums:
            currentMin = min(currentMin + n, n)
            currentMax = max(currentMax + n, n)
            res = max(res, abs(currentMin), currentMax)
        return res


# Kadane's DP algo
# basically find the min and the max possible subarray using the idea if it's better to start a new subarray completely
# or continue adding to the best subarray previously discovered

# note that it is faster to use if else over min max, but min max are more concise
