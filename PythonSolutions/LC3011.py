class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if bin(nums[i]).count("1") == bin(nums[i + 1]).count("1"):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                else:
                    return False

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                if bin(nums[i]).count("1") == bin(nums[i - 1]).count("1"):
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                else:
                    return False
        return True


# the approach here relies on not actually fully sorting the array, but rather thinking of the array as divided into
# segments each having a certain amount of set bits.
# numbers within each segment can be moved interchangeably, so the order within a segment is not relevant
# (as you could always sort that segment in theory)
# then the idea is if you can push the maximal value in the array to the last segment and the
# minimal value in the array to the first segment, then the segments individually are ordered in a way allowing sorting
# if you do need to swap but you cant due to the restriction, then return false; the segments are out of order

# an example
# 3 16 8 4 2 -> note this array is two segments: one consisting of 3 (2 set bits) and the other of 16 8 4 2 (1 set bit)
# first pass: 3 8 4 2 16. note the second segment can be sorted to 2 4 8 16 since they all have 1 set bit
# the second pass we get to 3 2 8 4 16 and run into an issue: to be sorted, 2 comes before 3, but we cannot
# perform the required swap since the two numbers have a different number of set bits.
# then return false.

# in this example, the segment consisting of 3 makes the array unsortable

# another example:
# 16 8 4 2 36 24
# note how 36 24 is a segment and 16 8 4 2 is a segment
# first pass 8 4 2 16 24 36. Note we don't need to move the 16 across segments. We need to move within segments (swapping 36 and 24 for example) but that is permitted
# a similar idea holds in the second pass
