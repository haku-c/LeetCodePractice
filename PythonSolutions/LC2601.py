class Solution:
    # def primeSubOperation(self, nums: List[int]) -> bool:
    #     def check(num):
    #         for i in range(2, int(num**0.5) + 1):
    #             if num % i == 0:
    #                 return False
    #         return True

    #     primeList = [0]
    #     for i in range(2, 1001):
    #         if check(i):
    #             primeList.append(i)

    #     def binarySearch(beforeNumber, currentNumber):
    #         start = 0
    #         end = len(primeList) - 1
    #         while start < end:
    #             mid = start + (end - start) // 2
    #             if currentNumber - primeList[mid] > beforeNumber:
    #                 start = mid + 1
    #             else:
    #                 end = mid - 1
    #         if currentNumber - primeList[start] > beforeNumber:
    #             return primeList[start]
    #         elif currentNumber - primeList[start - 1] > beforeNumber:
    #             return primeList[start - 1]
    #         else:
    #             return -1

    #     beforeNumber = 0
    #     for i in range(len(nums)):
    #         currentNumber = nums[i]
    #         subtract = binarySearch(beforeNumber, currentNumber)
    #         if subtract == -1:
    #             return False
    #         else:
    #             currentNumber = currentNumber - subtract
    #             beforeNumber = currentNumber
    #     return True

    # the inputs here are 1 to 1000. Since the input space is so small, we don't really need to do a binary search.
    # you can linear search between beforeNumber and currentNumber and that should be fast, and it will be easier to code.
    def primeSubOperation(self, nums: List[int]) -> bool:
        def check(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        beforeNumber = 0
        for i in range(len(nums)):
            currentNumber = nums[i]
            if currentNumber - beforeNumber >= 0:
                return False
            # don't forget to have subtracting 0 as an option
            subtract = 0
            for test in range(currentNumber - beforeNumber - 1, 1, -1):
                if check(test):
                    subtract = test
                    break
            currentNumber = currentNumber - subtract
            beforeNumber = currentNumber
        return True
