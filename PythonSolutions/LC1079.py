from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = -1

        def backtrack(used):
            # by incrementing at the start, you count the empty string on the first call.
            # Therefore you should start with -1 for res
            self.res += 1
            if sum(used.values()) == 0:
                return
            temp = used.items()
            for key, count in temp:
                if count > 0:
                    used[key] -= 1
                    backtrack(used)
                    used[key] += 1

        backtrack(Counter(tiles))
        return self.res
