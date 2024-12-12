from collections import defaultdict


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = defaultdict(int)
        for b, d in logs:
            line[b] += 1
            line[d] -= 1
        # print(line)
        maxPop = 0
        res = 0
        currentPop = 0
        for k, v in sorted(line.items()):
            currentPop += v
            if currentPop > maxPop:
                res = k
                maxPop = currentPop
        return res


# line sweep approach. Sweep from left to right means sort.
# compare with a global max and update res year accordingly.
# the key point of line sweeps is you only iterate through the endpoints of the ranges, skipping everything in between

# we want to add to currentPop everytime someone is born and subtract everytime someone passes away
# if we have born: 2000, born: 2001, pass away: 2010, pass away: 2050, born: 2060, pass away:2070
# then we have the population counts:
# 2000: 1, 2001: 2, 2010: 1, 2050: 0, 2060: 1, 2070: 0
# the values of the population don't fluctuate in betwee birth and death years, so there is no point in iterating over them
