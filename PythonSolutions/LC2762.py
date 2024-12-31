import heapq


# i didn't think growing backwards result in an O(n) algorithm, and I also forgot to subtract to account for double counting.
# i did think to use the formula n * (n+1) / 2
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        res = 0
        minVal = nums[0]
        maxVal = nums[0]
        for i in range(n):
            minVal = min(minVal, nums[i])
            maxVal = max(maxVal, nums[i])
            if maxVal - minVal > 2:
                res += (i - start + 1) * (i - start) // 2
                start = i
                maxVal = nums[i]
                minVal = nums[i]
                while start > 0 and abs(nums[i] - nums[start - 1]) <= 2:
                    start -= 1
                    minVal = min(minVal, nums[start])
                    maxVal = max(maxVal, nums[start])

                # you can put a check here to skip changing res if i == start and it will be slightly faster. Important to subtract values in the new window
                res -= (i - start + 1) * (i - start) // 2

        res += (n - start + 1) * (n - start) // 2

        return res


# this other solution uses a sliding window approach and is slower because you pop from the heaps as you shrink the window from the left
# def continuousSubarrays(self, nums: List[int]) -> int:
#     n = len(nums)
#     start = 0
#     end = 0
#     res = 0
#     largest = []
#     smallest = []
#     while end < n:
#         heapq.heappush(largest, (-nums[end], end))
#         heapq.heappush(smallest, (nums[end], end))

#         while start < end and -largest[0][0] - smallest[0][0] > 2:
#             start += 1
#             while largest and largest[0][1] < start:
#                 heapq.heappop(largest)
#             while smallest and smallest[0][1] < start:
#                 heapq.heappop(smallest)

#         res += end - start + 1
#         end += 1

#     return res
