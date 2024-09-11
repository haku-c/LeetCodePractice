# this implementation uses string manipulation and the built in binary conversion in python
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start)
        e = bin(goal)
        sLen = len(s)
        eLen = len(e)

        if sLen > eLen:
            e = "".join(["0" * (sLen - eLen), e[2:]])
            s = s[2:]
        else:
            s = "".join(["0" * (eLen - sLen), s[2:]])
            e = e[2:]

        res = 0
        for i in range(len(s)):
            if s[i] != e[i]:
                res += 1
        return res


# a more barebones approach with bit shifting is below. Basically, we do bitwise and to find the rightmost bit value and compare
# shift right to move the bits one to the right and reduce the size of what is being compared.
# Note the smaller value might have less bits overall. Anding 0 with 1 gets 0, so this effectively left pads the smaller value
# so you can continue comparing the bits from the larger number
# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         maxi = max(start, goal)
#         res = 0
#         while maxi:
#             if (start & 1) != (goal & 1):
#                 res = res + 1
#             start = start >> 1
#             goal = goal >> 1
#             maxi = maxi >> 1
#         return res
