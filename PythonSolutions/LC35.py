def maxSubArray(self, nums: List[int]) -> int:
    # original solution with prefix array
    # prefix = [[0] for i in range(len(nums))]
    # res = lowest = prefix[0] = nums[0]
    # for i in range(1,len(nums)):
    #     prefix[i] = prefix[i-1] + nums[i]
    #     res = max(res, prefix[i])
    #     res = max(res, prefix[i] - lowest)
    #     lowest = min(lowest, prefix[i])
    # return res

    # optimized solution leveraging the nature of the problem
    res = nums[0]
    currentSum = 0
    for n in nums:
        # if the current working sum is negative and our value is greater than that, just start at the current value
        # this is because including the values in the current sum can only make the current sum lower
        if currentSum < 0 and n > currentSum:
            currentSum = n
        else:
            # otherwise, the current working sum is positive and we can continue the chain
            currentSum += n
        # always check if the current sum is greater than our tracked result
        res = max(res, currentSum)
    return res
