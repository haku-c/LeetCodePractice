class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        # approach: sort numbers, cache results if sqrt of current has a past entry, then you know current
        # is part of some streak
        table = {}
        res = -1
        for i in nums:
            if i**0.5 in table:
                streak = table[i**0.5] + 1
                res = max(streak, res)
                table[i] = streak
            else:
                table[i] = 1
        return res


# you dont need the dictionary, you can use a nested loop and a set. Note how you don't have to sort if you do this
# O(n) space
# class Solution:
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         nums = set(nums)
#         max_length = 0
#         for num in nums:
#             length = 0
#             current = num
#             while current in nums:
#                 length += 1
#                 current = current**2
# the check here for length > 1 has a meaningful impact on performance. Don't want to check when there is no length update
#             if length > 1:
#                 max_length = max(max_length, length)
#         return max_length if max_length > 1 else -1
