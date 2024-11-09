class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # res = [0] * 26
        # for num in candidates:
        #     currentBinary = bin(num)[2:]
        #     for i in range(len(currentBinary)):
        #         res[25 - i] += int(currentBinary[len(currentBinary) - 1 -i])
        # return max(res)
        res = 1
        for i in range(24):
            curr = 0
            for num in candidates:
                if (num & (1 << i)) != 0:
                    curr += 1
            res = max(res, curr)
        return res


# 1 << i is a bit mask. Instead of directly converting the whole number using bin, we can take the and of the mask to find out
# if that indexed bit is set.
