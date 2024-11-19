from collections import Counter


# solution not using a counter uses a prefix sum. I code that below this one
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        res = 0
        windowSum = 0
        start = 0
        for i in range(len(nums)):
            currentNumber = nums[i]
            counts[currentNumber] += 1
            windowSum += currentNumber
            while counts[currentNumber] > 1 or i - start + 1 > k:
                windowSum -= nums[start]
                counts[nums[start]] -= 1
                start += 1
            if i - start + 1 == k:
                res = max(res, windowSum)

        return res


# the below solution is faster but uses more memory to store the positions which prior keys have ocurred
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        start = 0
        prefix = [0] * (n + 1)
        last = {}
        for i in range(0, n):
            current = nums[i]
            prefix[i + 1] = prefix[i] + current

            if current in last and start <= last[current]:
                start = last[current] + 1

            last[current] = i
            if i - start + 1 == k:
                res = max(res, prefix[i + 1] - prefix[start])
                start += 1
        return res
