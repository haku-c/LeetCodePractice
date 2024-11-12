class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # the interesting cases are when we need to OR to get a set bit within the number
        window = 0
        res = float("inf")
        start = 0
        freq = [0] * 32

        def convertToInt(binArray):
            integer = 0
            for i in range(32):
                n = binArray[i]
                if n > 0:
                    integer += 2 ** (31 - i)
            return integer

        for i in range(len(nums)):
            bitString = format(nums[i], "032b")
            for ind in range(32):
                freq[ind] += int(bitString[ind])

            window = convertToInt(freq)
            while window >= k and start <= i:
                res = min(res, i - start + 1)
                bitString = format(nums[start], "032b")
                for ind in range(32):
                    freq[ind] -= int(bitString[ind])
                window = convertToInt(freq)
                start += 1
        if res == float("inf"):
            return -1
        return res


# slow solution, most likely due to the conversion from the bit array to integer.
# a helpful thing to use is the bit array for ors
