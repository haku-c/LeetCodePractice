class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAnd = 0
        past = False
        current = 0
        res = 0
        for i in nums:
            if i > maxAnd:
                maxAnd = i
                current = 1
                past = True
                res = 1
            elif i == maxAnd and not past:
                past = True
                current = 1
                res = max(res, current)
            elif i == maxAnd:
                current += 1
                res = max(res, current)
            else:
                past = False
                current = 0
        return res