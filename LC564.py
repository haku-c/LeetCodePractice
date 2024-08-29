class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def closer(n, n1, n2):
            if int(n1) > int(n2):
                higher = n1
                lower = n2
            else:
                higher = n2
                lower = n1
            if higher == n:
                return lower
            elif lower == n:
                return higher
            else:
                return (
                    higher
                    if abs(int(n) - int(higher)) < abs(int(n) - int(lower))
                    else lower
                )

        def mirror(s):
            length = len(s)
            if length % 2 == 0:
                res = s[0 : length // 2] + s[0 : length // 2][::-1]
            else:
                res = s[0 : length // 2 + 1] + s[0 : length // 2][::-1]
            return res

        def decFirstHalf(s):
            length = len(s)
            if length % 2 == 0:
                f = int(s[0 : length // 2]) - 1
                res = str(f) + str(f)[::-1]
            else:
                f = int(s[0 : length // 2 + 1]) - 1
                res = str(f) + str(f)[0 : length // 2][::-1]
            return res

        def incrFirstHalf(s):
            length = len(s)
            if length % 2 == 0:
                f = int(s[0 : length // 2]) + 1
                res = str(f) + str(f)[::-1]
            else:
                f = int(s[0 : length // 2 + 1]) + 1
                res = str(f) + str(f)[0 : length // 2][::-1]
            return res

        def p999(s):
            length = len(s)
            above = "9" * length
            below = "9" * (length - 1)
            return str(closer(s, above, below))

        def p101(s):
            length = len(s)
            above = 10**length + 1
            below = 10 ** (length - 1) + 1
            return str(closer(s, above, below))

        if len(n) == 1:
            return str(int(n) - 1)

        dec = decFirstHalf(n)
        incr = incrFirstHalf(n)
        mirr = mirror(n)
        p1 = p101(n)
        p9 = p999(n)
        res = closer(n, dec, incr)
        res = closer(n, res, mirr)
        res = closer(n, res, p1)
        res = closer(n, res, p9)
        return res
