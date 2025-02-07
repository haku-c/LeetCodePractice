from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors = defaultdict(int)
        res = []
        unique = 0
        for ball, color in queries:
            if balls[ball] != 0:
                oldColor = balls[ball]
                colors[oldColor] -= 1
                if colors[oldColor] == 0:
                    unique -= 1
            colors[color] += 1
            if colors[color] == 1:
                unique += 1
            balls[ball] = color
            res.append(unique)
        return res


# pretty straightforward solution. You don't have to use defaultdicts if you want to use getOrDefault. Up to you
# if this is the first time we've seen this color, increment the unique count.
# if we have 0 of this color, decrement the unique count
# use hashmaps to store because the number of balls and the number of colors is very large 10**9
