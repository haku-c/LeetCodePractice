# line sweep version. Just count the number of distinct intervals using line sweep


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        overlaps = defaultdict(int)
        distinct = 0
        for x, y in ranges:
            overlaps[x] += 1
            overlaps[y] -= 1
        pref = 0
        for _, val in sorted(overlaps.items()):
            pref += val
            if pref >= 0:
                started = True
            if pref <= 0 and started:
                distinct += 1
                started = False

        return (2**distinct) % (10**9 + 7)


# sorting version
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        distinct = 1
        right = 1
        ranges = sorted(ranges)
        _, end = ranges[0]
        while right < len(ranges):
            rightStart, rightEnd = ranges[right]
            # if distinct intervals, create new interval
            if rightStart > end:
                distinct += 1
                end = rightEnd
            # merge intervals if overlap
            elif rightStart <= end:
                end = max(rightEnd, end)
            right += 1

        return (2**distinct) % (10**9 + 7)
