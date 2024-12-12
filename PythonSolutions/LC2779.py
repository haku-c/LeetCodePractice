# class Solution:
#     def maximumBeauty(self, nums: List[int], k: int) -> int:
#         left = 0
#         current = 0
#         nums.sort()
#         leftLimit, rightLimit = nums[0] - 2 * k, nums[0] + 2 * k
#         size = 0
#         res = 1
#         for right in range(len(nums)):
#             if nums[right] <= rightLimit and nums[right] >= leftLimit:
#                 size += 1
#             else:
#                 while nums[right] > rightLimit:
#                     current += 1
#                     rightLimit = nums[current] + 2 * k
#                 # adjust the left bound
#                 leftLimit = rightLimit - 2 * k
#                 # increase size by 1 since we can now include nums[right] in our window
#                 size += 1
#                 # remove numbers from the window that no longer are in bound
#                 while nums[left] < leftLimit:
#                     size -= 1
#                     left += 1
#             # print(nums)
#             # print("left index is: " + str(left) + " which is: " + str(nums[left]))
#             # print("right index is: " + str(right) + " which is: " + str(nums[right]))
#             # print("current index is: " + str(current) + " which is: " + str(nums[current]))
#             # print("size: " + str(size))
#             # print("---")
#             res = max(size, res)
#         return res


# here's a version without the size variable, since you can just calculate it directly from right and left
# you can also calculate the bounds directly
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        left = 0
        current = 0
        nums.sort()
        leftLimit, rightLimit = nums[0] - 2 * k, nums[0] + 2 * k
        res = 1
        for right in range(len(nums)):
            while nums[right] > rightLimit:
                current += 1
                rightLimit = nums[current] + 2 * k
            leftLimit = rightLimit - 2 * k
            while nums[left] < leftLimit:
                left += 1
            # print(nums)
            # print("left index is: " + str(left) + " which is: " + str(nums[left]))
            # print("right index is: " + str(right) + " which is: " + str(nums[right]))
            # print("current index is: " + str(current) + " which is: " + str(nums[current]))
            # print("size: " + str(size))
            # print("---")
            res = max(res, right - left + 1)
        return res


# The whole idea here is to find the largest window where every number fits within some bound that is 2*k wide.

# here's a case i did not consider when first going through this problem:
# 10, 59, 86 k = 23
# it is not enough to rule out 59 and 86 being able to form a beautiful subsequence just because 86 - 59 = 27 > 23
# note we can transform the 59 to 82 and then the 86 to 82, resulting in a subsequence of length 2
# this means the center of the bound does not necessarily need to be a number in the actual array.
# since we transformed 59 -> 82, then the leftLimit and rightLimit are fixed to 82. Since 86 is within that bound (82-23, 82+23), we have a subsequence

# when we go through the algorithm, we need to change the bound when the rightmost number exceeds the right bound.
# since the list is sorted, we know every number after nums[right] will also exceed our current bound
# we know we need to increase the current to something. The key is to increase the right bound the most possible to include nums[right]
# this is nums[current] + 2*k. Why?
# we center our bound to a number in our list. Then we change that number to be the largest possible after an operation. That means nums[current] + k
# however, any number above can also reduce their value by k. This means the true rightLimit for the bounds centered at nums[current] is
# nums[current] + 2 * k
# of course, the leftLimit is also determined by this; leftLimit = rightLimit - 2 * k
