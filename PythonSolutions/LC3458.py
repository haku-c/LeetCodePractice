class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:

        endpoints = {}
        for i in range(len(s)):
            letter = s[i]
            if letter not in endpoints:
                endpoints[letter] = [i, i]
            else:
                endpoints[letter][1] = i

        for c in endpoints:
            start, end = endpoints[c]
            for j in set(s[start:end]):
                start, end = endpoints[c]
                currentStart, currentEnd = endpoints[j]
                endpoints[c] = [min(start, currentStart), max(end, currentEnd)]

        # print(endpoints)

        entry = [0 for _ in range(len(s))]

        # dynamic programming, where entry[i] represents the max disjoint substrings you can form with s[0:i] (inclusive of i
        # the trick here is we can add a new disjoint interval if we reach the endpoint of one of the letters at the current index)
        # if this is the case, we can form an interval and block out the rest of the string we have seen
        # since we can't have overlapping intervals, if we take this new interval, we can only form intervals
        # with the letters from index 0 up to the start of the new interval. Since we already stored the max value
        # of intervals possible formed from 0 to the start, we can use that value
        for i, c in enumerate(s):
            # an extra check to make sure that we don't return true if the interval is the entire string -> endpoints[c] = 0, len(s) - 1
            if endpoints[c][1] == i and (endpoints[c][0] != 0 or i != len(s) - 1):
                entry[i] = max(entry[endpoints[c][0] - 1] + 1, entry[i - 1])
            else:
                entry[i] = entry[i - 1]

        # print(entry)
        return entry[-1] >= k

        # # optimal(s) = max(1 + optimal(use c -> s shrink), optimal(dont use c))
        # # opt(interval) = max(1, intervals in interval)
        # first, end = {}, {}
        # for i, c in enumerate(s):
        #     if c not in first:
        #         first[c] = i
        #     end[c] = i

        # print(first)
        # print(end)
        # # expand first and end interval for each character, O(26*N)
        # for c in first:
        #     for i in range(first[c], end[c]):
        #         m = s[i]
        #         first[c] = min(first[c], first[m])
        #         end[c] = max(end[c], end[m])

        # # dp[i] means maximal disjoint substrings we can form using s[:i]
        # n = len(s)
        # dp = [0 for _ in range(n + 1)]
        # for i, c in enumerate(s):
        #     dp[i + 1] = dp[i]
        #     if end[c] == i and (first[c] != 0 or i != n - 1):
        #         dp[i + 1] = max(dp[i + 1], 1 + dp[first[c]])
        # return dp[-1] >= k
