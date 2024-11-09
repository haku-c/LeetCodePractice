class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # requires the time represented by s1 comes before the time represented by s2
        def timeDifference(s1, s2):
            hh1 = int(s1[0:2])
            mm1 = int(s1[3:])
            hh2 = int(s2[0:2])
            mm2 = int(s2[3:])
            minutes = 0
            if mm2 >= mm1:
                minutes += mm2 - mm1
            else:
                minutes += (60 - mm1) + mm2
                hh1 += 1
            if hh1 != hh2:
                minutes += (hh2 - hh1) * 60
            return minutes

        ordered = sorted(timePoints)
        res = float("inf")
        for index in range(len(ordered) - 1):
            prev = ordered[index]
            nextTime = ordered[index + 1]
            res = min(res, timeDifference(prev, nextTime))
        # this is the edge case where with wraparound the minutes between the largest and smallest time is the minimum
        # ex/ 00:01, HHMM, HHMM, HHMM, 23:59 which has a minimum time of 2 minutes to go from 23:59 to 00:01 aka 24:01
        temp = str(int(ordered[0][0:2]) + 24) + ordered[0][2:]
        res = min(res, timeDifference(ordered[-1], temp))
        return res
