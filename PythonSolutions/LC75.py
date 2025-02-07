class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        # print(counts)
        nums[0 : counts[0]] = [0] * counts[0]
        nums[counts[0] : counts[0] + counts[1]] = [1] * counts[1]
        nums[counts[0] + counts[1] : counts[0] + counts[1] + counts[2]] = [2] * counts[
            2
        ]


# this uses countsort and is not one pass
# for a one pass solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroBound = 0
        twoBound = len(nums) - 1
        i = 0
        while i <= twoBound:
            curr = nums[i]
            if curr == 0:
                nums[zeroBound], nums[i] = nums[i], nums[zeroBound]
                zeroBound += 1
                i += 1
            elif curr == 1:
                i += 1
            else:
                nums[twoBound], nums[i] = nums[i], nums[twoBound]
                twoBound -= 1
