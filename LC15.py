def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    soln = []
    nums.sort()
    for index, value in enumerate(nums):
        if value > 0:
            break

        if index > 0 and nums[index - 1] == value:
            continue

        start, end = index + 1, len(nums) - 1
        while start < end:
            s = nums[start] + nums[end] + value
            if s == 0:
                soln.append([value, nums[start], nums[end]])
                start += 1
                end -= 1
                while (nums[start] == nums[start - 1]) and start < end:
                    start += 1
            elif s > 0:
                end -= 1
            else:
                start += 1
    return soln


# this solution relies on the fact that you sort the array. When the sum is greater or less than zero you know which direction you need to change the numbers in your set.
