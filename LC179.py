class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        nums = sorted(nums, key=lambda x: str(x) * 10, reverse=True)
        for n in nums:
            res += str(n)
        if nums[0] == 0:
            return "0"
        return res


# strings in python are compared lexicographically from left to right. However, if there is a tie and one of the strings are exhausted, the shorter string is smaller
# for the cases such as 43, 4313, we need to make it so the comparator works such that 434313 is returned and not 341343
# that is 43 > 4313.
# if we just compared lexicographically, this would not work.
# hence, we need to extend 43 to 4343 > 4313 lexicographically.
# logically, if we put 43 first, then we can get another 43 in the next two spots as opposed to just using 4313.
# this implies we should repeat the matching prefix between the two strings when they are not the same length
# because of the behavior of string comparison (terminating when we run out of chars in one) we can just repeat both strings 10 times.
# repeat 10 times since the extent of the values is 10^9. If we do a number less than 10, then a single digit like 9 will not be extended all the way in some scenarios

# If I wasn't using python3, I would instead use the custom comparator taking 2 strings a b and check the value of their concatenation:
# lamda a,b: return a + b > b + a
# or something to the effect of a + b compareTo b + a
