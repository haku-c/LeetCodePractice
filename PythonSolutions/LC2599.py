# You are given a 0-indexed integer array nums. You can apply the following operation any number of times:

#     Pick any element from nums and put it at the end of nums.

# The prefix sum array of nums is an array prefix of the same length as nums such that prefix[i] is the sum of all the integers nums[j] where j is in the inclusive range [0, i].

# Return the minimum number of operations such that the prefix sum array does not contain negative integers. The test cases are generated such that it is always possible to make the prefix sum array non-negative.

import heapq


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        pref = 0
        h = []
        res = 0
        for n in nums:
            pref += n
            if n < 0:
                heapq.heappush(h, n)
            while pref < 0:
                pref -= heapq.heappop(h)
                res += 1
        return res


# note: consider cases where the prefix sum goes negative: you want to remove the most negative number in the prefix first. Hence, use a queue
# case: 6, -6, -3, 3, 1, 5, -4, -3, -2, -3, 4, -1, 4, 4, -2, 6, 0
