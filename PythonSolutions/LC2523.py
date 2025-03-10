class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # sieve of eratosthenes approach
        nums = list(range(left, right + 1))
        for i in range(2, int((right + 1) ** 0.5) + 1):
            current = (left / i) * i
            for c in range(current, right + 1, i):
                if c - left >= 0 and c != i:
                    nums[c - left] = 0
        l = r = -1
        res = [l, r]
        diff = float("inf")
        for i in range(right + 1 - left):
            if nums[i] > 1:
                if l != -1 and nums[i] - l < diff:
                    diff = nums[i] - l
                    res = [l, nums[i]]
                    if diff <= 2:
                        return res
                l = nums[i]

        return res

    # a much faster solution relying on the fact that wide enough intervals must have at least one pair of primes a distance of 2 apart
    # def isPrime(n):
    #     if n < 2:
    #         return False
    #     for i in range(2, int(n**.5) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

    # diff = float('inf')
    # l = -1
    # res = [l, -1]
    # for i in range(left, right + 1):
    #     if isPrime(i):
    #         if l != -1:
    #             if i - l < diff:
    #                 diff = i - l
    #                 res = [l, i]
    #                 # only works because of early stoppage
    #                 if diff <= 2:
    #                     return res
    #         l = i
    # return res
