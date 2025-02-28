import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # sort array
        # exclude all numbers that are currently correct
        # take the difference for all numbers less than value and push them up
        # take the difference for all number greater than value and push them down
        # difference of queries[i] * number of elements in left and actual sum of elements in left
        # compute sums using prefix array
        nums.sort()
        n = len(nums)
        res = [0] * len(queries)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        for i in range(len(queries)):
            curr = 0
            val = queries[i]
            left = bisect.bisect_left(nums, val)
            curr += (left * val) - pref[left]
            right = bisect.bisect_right(nums, val)
            curr += (pref[-1] - pref[right]) - ((n - right) * val)
            res[i] = curr
        return res


# using the prefix array with an extra element is good because we dont need to do checks if
# the bisect goes to the end of the array or not. (since pref[len(nums)] is in bounds)
# if the right values ends up being the length, then we just add 0 to the result: right = n and plug into the assignment
# if the left value is the length then right is length, too
# left value being length indicates all entries in nums is less than the value. Therefore, we can just take one differencec
# between the sum of the entire array and value * length

# ACTUALLY YOU ONLY NEED TO BISECT ONCE
# we already account for the numbers that don't need to change on the right, since we take the desired value * number of positions
# since bisect left gets you the first occurence of val, if there are duplicate values we can account for them in the second
# step where (pref[-1] - pref[right]) - ((n - right) * val)

# OPTIMAL:
import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # sort array
        # exclude all numbers that are currently correct
        # take the difference for all numbers less than value and push them up
        # take the difference for all number greater than value and push them down
        # difference of queries[i] * number of elements in left and actual sum of elements in left
        # compute sums using prefix array
        nums.sort()
        n = len(nums)
        res = []
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        for i in range(len(queries)):
            val = queries[i]
            left = bisect.bisect_left(nums, val)
            # curr = (
            #     (left * val) - pref[left] + (pref[-1] - pref[left]) - ((n - left) * val)
            # )
            # simplify formula
            curr = 2 * (left * val - pref[left]) + pref[-1] - (n * val)
            res.append(curr)
        return res
