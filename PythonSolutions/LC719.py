class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxDistance = nums[-1] - nums[0]

        def countPairs(diff):
            count = 0
            i = 0
            j = 1
            while i < len(nums):
                while (j < len(nums)) and ((nums[j] - nums[i]) <= diff):
                    j += 1
                # the number of pairs with difference less than diff must be at least as much as the past iteration -1 since
                # you incremented i (and nums is sorted). You are increasing the start value and keeping the end value
                # fixed.
                count += j - i - 1
                i += 1
            return count

        start = 0
        end = maxDistance
        while start < end:
            current = (end + start) // 2
            c = countPairs(current)
            if c >= k:
                end = current
            else:
                start = current + 1

        return start


# binary search on the possible solutions
# also efficiently count the number of pairs within the search space
