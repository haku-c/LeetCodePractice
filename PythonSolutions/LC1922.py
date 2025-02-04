import math


class Solution:

    # fast exponentiation with bit manipulation and modulation
    # the fast exponentiation is useable because we can multiply by higher powers of 5 in a O(logn) exponentiation
    # 5^10 = (5^2)^5
    #      = 25.25^4
    #      = 25.(25^2)^2
    #      = 25.(625)^2
    #      = 25.625.625
    def countGoodNumbers(self, n: int) -> int:
        even = math.ceil(n / 2)
        odd = int(n / 2)

        def powerOptimised(a, n):
            ans = 1

            while n > 0:
                last_bit = n & 1

                # Check if current LSB
                # is set
                if last_bit:
                    ans = ans * a
                a = a * a % (10**9 + 7)

                # Right shift
                n = n >> 1

            return ans

        return int(powerOptimised(5, even) * powerOptimised(4, odd)) % (10**9 + 7)
