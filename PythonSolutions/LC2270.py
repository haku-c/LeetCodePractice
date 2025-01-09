class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # pref = [0] * n
        # pref[0] = nums[0]
        # for i in range(1, n):
        #     pref[i] = pref[i-1] + nums[i]
        # res = 0
        # total = pref[-1]
        # for i in range(n-1):
        #     if pref[i] >= (total-pref[i]):
        #         res += 1
        # return res
        res = 0
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        for i in range(n - 1):
            leftSum = nums[i] + leftSum
            rightSum = rightSum - nums[i]
            if leftSum >= rightSum:
                res += 1
        return res
