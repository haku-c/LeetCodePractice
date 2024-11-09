from math import ceil


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        observed = sum(rolls)
        target = (mean * (n + m)) - observed
        if ceil(target / n) > 6 or n > target:
            return []
        num = target // n
        current = num * n
        res = [num + (1 if i < target - current else 0) for i in range(n)]
        # for i in range(target-current):
        #     res[i] = num + 1
        return res
