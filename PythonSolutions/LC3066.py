import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while len(nums) >= 2 and nums[0] < k:
            heapq.heappush(nums, heapq.heappop(nums) * 2 + heapq.heappop(nums))
            res += 1
        return res


# very straightforward heap question.
