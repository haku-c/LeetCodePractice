from fractions import Fraction
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        finalFract = 0
        s = re.split("\+|\-", expression)
        s = list(filter(None, s))
        ops = []
        if expression[0] != "-":
            ops.append("+")
        for c in expression:
            if c == "-" or c == "+":
                ops.append(c)
        for fract in s:
            op = ops.pop(0)
            if op == "+":
                finalFract += Fraction(fract)
            else:
                finalFract -= Fraction(fract)
        res = str(finalFract)
        # res = str(Fraction(finalFract).limit_denominator())
        if "/" not in res:
            res = res + "/1"
        return res
