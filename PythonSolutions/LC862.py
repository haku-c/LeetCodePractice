import heapq


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        current = 0
        res = float("inf")
        h = []
        for i in range(len(nums)):
            current += nums[i]
            if current >= k:
                res = min(res, i + 1)
            while h:
                topSum, ind = h[0]
                if current - topSum < k:
                    break
                heapq.heappop(h)
                res = min(res, i - ind)
            heapq.heappush(h, (current, i))
        return -1 if res == float("inf") else res


# we can find the sum of any subarray using the following idea: prefix[i] - prefix[n] is the sum of values from index n + 1 to i
# then we can use this idea to quickly compute subarray sums and check if they are equal to k
# we need to test potential values of n by testing if currentSum - prefix[n] >= k
# if we take it so prefix[n] is the lowest prefix seen,
# then we can continue taking the lowest until currentSum - prefix[n] < k,
# which means prefix[n] is too big. Along the way, recompute the result since we have a valid subarray.
# iterating every possible subarray combo is O(n^2), so using this ordering of the prefixes is better.
