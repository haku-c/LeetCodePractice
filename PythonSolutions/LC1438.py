from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mins = deque()
        maxs = deque()
        start = 0
        res = 0
        for end in range(len(nums)):
            current = nums[end]
            while maxs and current > maxs[-1]:
                maxs.pop()
            maxs.append(current)
            while mins and current < mins[-1]:
                mins.pop()
            mins.append(current)
            while maxs[0] - mins[0] > limit:
                left = nums[start]
                if left == mins[0]:
                    mins.popleft()
                if left == maxs[0]:
                    maxs.popleft()
                start += 1
            res = max(res, end - start + 1)
        return res
