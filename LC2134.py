class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count1 = 0
        count0 = 0
        length = len(nums)
        for n in nums:
            if n == 1:
                count1 += 1
        for i in range(count1):
            if nums[i] == 0:
                count0 += 1
        min0 = count0
        start = 0
        end = count1 % length
        while start < length:
            if nums[start] == 0:
                count0 -= 1
            if nums[end] == 0:
                count0 += 1
            start += 1
            end = (end + 1) % length
            min0 = min(min0, count0)

        return min0


# 2 passes
# 1 pass to determine the size of the sliding window
# the other pass to find the window that has the least amount of 0s.
