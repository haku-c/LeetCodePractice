class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums2) & 1:
            for num in nums1:
                res ^= num
        if len(nums1) & 1:
            for num in nums2:
                res ^= num
        return res


# Think about the combinations aspect:
# say nums1 = [1,2,3] nums2 = [10,5]
# in the final result we would have (1 xor 10 xor 1 xor 5) xor (2 xor 10 xor 2 xor 5) xor (3 xor 10 xor 3 xor 5)
# if we do some term rearranging, we can see we have 1 appearing twice, 2 appearing twice, 3 appearing twice
# 5 appearing three times, 10 appearing three times
# this means every number in nums1 appears len(nums2) times and every number in nums2 appears len(nums1) times

# because of the way xor works, if we take xor of the same number for example 1 ^ 1, that is 0
# so if we have an even number of appearances for a certain number, that just zeroes out.
# example: 1 ^ 1 ^ 1 ^ 1 = (1 ^ 1) ^ (1 ^ 1) = 0 ^ 0 = 0
# similarly, if we have an odd number of appearances for a certain number, the result of all those xors is just that same number!
# example: 1 ^ 1 ^ 1 = (1 ^ 1) ^ 1 = 0 ^ 1 = 1

# if the length of nums2 is odd, we know every number in nums1 appears in the xor of nums3
# if the length of nums1 is odd, every number in nums2 appears in the xor of nums3
# if length of nums2 is even, then we don't have to do anything with numbers in nums1 since the xors would cancel.
# if length of nums1 is even, then we don't have to do anything with numbers in nums2 since the xors would cancel.
