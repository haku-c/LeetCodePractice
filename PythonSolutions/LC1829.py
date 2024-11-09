class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix = nums[0]
        for i in range(1, len(nums)):
            prefix = nums[i] ^ prefix
        res = [0] * n
        maximum = int("1" * (maximumBit), 2)

        for i in range(n):
            res[i] = maximum - prefix
            prefix = prefix ^ nums[n - 1 - i]

        return res


# xor is reversible, hence you can just reverse the operation when you do your queries (prefix ^ nums[n - 1 -i])
# maximum - prefix is essentially flipping all the 1s to 0s and 0s to 1s. You don't want to use the not bitwise operation (~)
# because python will take the signed integer.
# The maximum being the integer version of "1" * maximumBit gives a ceiling to subtract from
