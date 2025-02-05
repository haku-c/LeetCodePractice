from collections import defaultdict


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pref = defaultdict(int)
        for start, end in intervals:
            pref[start] += 1
            pref[end] -= 1
        started = False
        res = []
        currentCount = 0
        for key, count in list(sorted(pref.items())):
            currentCount += count
            if currentCount >= 0 and not started:
                started = True
                left = key
            if currentCount <= 0 and started:
                started = False
                right = key
                res.append([left, right])
        return res


# here's an alternate to the linesweep that i like better
# directly sort the intervals by start time and repeatedly modify the last entry in the result if we need to merge
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         intervals.sort(key=lambda x: x[0])

#         merged = []
#         for interval in intervals:
#             # if the list of merged intervals is empty or if the current
#             # interval does not overlap with the previous, simply append it.
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#                 # otherwise, there is overlap, so we merge the current and previous
#                 # intervals.
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged
