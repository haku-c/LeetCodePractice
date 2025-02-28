class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (len(nums) * min(nums))

        # i do not like this question


# here's an explanation for why the above formula works

# suppose there are k elements, the sum of original array is s, the minimum move is m, eventually all the elements become e,
# we know each move contributes (k-1) to the sum, so we have:
# s + (k-1)*m = k*e
# for the minimum element min, it must be added to m times, i.e.
# min + m = e
# The two equations above would give us m = s - k*min

# s + km - m = k(min) + km
# s -k(min) = m
