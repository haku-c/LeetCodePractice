import math


class Solution:
    def minSteps(self, n: int):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n / 2
        # check odd numbers in the range of 3 to the sqrt of the number
        for i in range(3, int(math.sqrt(n) + 1), 2):
            while n % i == 0:
                factors.append(i)
                n = n / i
        if n > 2:
            factors.append(n)

        # prime factorization
        # 5 * 2 -> 2 pastes of 5
        # 50 = 5 * 5 * 2 -> get to 10, paste 5 times. 10 can be formed by 2 paste 5 times
        # 330 = 5 * 2 * 3 * 11 -> get to 2, copy then paste 2 times, copy then paste 4 times, copy then paste 10 times
        # 75 = 5 * 5 * 3 -> get to 3, copy and paste 5, paste 5
        # sum of price factorization

        return int(sum(factors))


if __name__ == "__main__":
    x = Solution()
    print(x.minSteps(120))
