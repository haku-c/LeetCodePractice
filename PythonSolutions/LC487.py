class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = zeroSwap = oneSwap = 0
        for num in nums:
            if num == 1:
                zeroSwap += 1
                oneSwap += 1
            else:
                oneSwap = zeroSwap + 1
                zeroSwap = 0
            if oneSwap > res:
                res = oneSwap
        return res

    # we want to track the max len consecutive sequence ending in the current number.
    # we track a version with no swaps
    # and a version with one swap
    # reset the length of the no swap if it ends with a zero
    # increment both if end with one
    # try to continue the one swap sequence if current is zero

    # version with tables O(n) space
    # if nums[0] == 1:
    #     table[0][0] = 1
    #     table[1][0] = 1
    # else:
    #     table[0][0] = 0
    #     table[1][0] = 1
    # for i in range(1,n):
    #     num = nums[i]
    #     if num == 1:
    #         table[0][i] = table[0][i-1] + 1
    #         table[1][i] = table[1][i-1] + 1
    #     else:
    #         table[0][i] = 0
    #         table[1][i] = table[0][i-1] + 1
    # print(table)
    # return max(table[1])
