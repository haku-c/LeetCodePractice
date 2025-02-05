from collections import defaultdict


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = 0
        n = len(nums)
        counts = defaultdict(int)
        res = [0] * (n - k + 1)
        distinct = 0
        while start < n - k + 1:
            counts[nums[end]] += 1
            if counts[nums[end]] == 1:
                distinct += 1
            if end - start + 1 == k:
                # print(counts.items())
                res[start] = distinct
                counts[nums[start]] -= 1
                if counts[nums[start]] == 0:
                    distinct -= 1
                start += 1
            end += 1
        return res


# Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].

# Return the array ans.
