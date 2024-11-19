class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        windowSum = 0
        res = float("inf")
        for i in range(len(nums)):
            windowSum += nums[i]
            while windowSum >= target:
                res = min(res, i - start + 1)
                windowSum -= nums[start]
                start += 1

        return 0 if res == float("inf") else res


# sliding window approach: expand the window to the right until the window's sum is >= k. Then shrink from the left until the window's sum is less
