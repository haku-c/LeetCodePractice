class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = max(nums)

        def check(limit, nums):
            n = len(nums)
            carryover = 0
            for i in range(n - 1, 0, -1):
                if nums[i] + carryover > limit:
                    carryover = (nums[i] + carryover) - limit
                else:
                    carryover = 0
            return (nums[0] + carryover) <= limit

        while start <= end:
            mid = start + (end - start) // 2
            if check(mid, nums):
                end = mid - 1
            else:
                start = mid + 1
        return start


# this is the binary search solution. suboptimal. not sure why the hint leads you to it.
# linearish greedy is possible (and was my original thought)
import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref = 0
        res = 0
        for i in range(len(nums)):
            pref += nums[i]
            res = max(res, math.ceil(pref / (i + 1)))

        return res


# this solution is actually very elegant: since you can only decrease values by transfering from right to left,
# if we encounter some max value on the left, we cannot redistribute using it (think of it as some fixed max value)
# hence if a fixed number is greater than our redistributed result, we still need to take that as the answer

# so, if we encounter [10,1]
# the 10 remains our max even if we would prefer to redistribute 11 across 2 numbers
