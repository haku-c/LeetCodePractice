from collections import defaultdict
from math import comb


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                counts[nums[i] * nums[j]] += 1
        res = 0
        # print(counts)
        for prod, count in counts.items():
            res += math.comb(count, 2) * 8
        return res


# each tuple pair combination adds 8 to the result. we can choose 2 pairs of numbers that have the same product at a time
# for example, if your pairs are (6,10), (20,3), (15,4) you can choose 2 of these 3 to form pairs at once:
# 1. (6,10), (20,3) 2. (6,10), (15,4) 3. (20,3), (15,4)
# each set of (a,b) (c,d) can be permuted 8 times.
# so it's (# valid tuples choose 2) * 8
# in the example, 3 * 8 = 24
# note it's O(n^2) but n is small
