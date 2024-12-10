from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        curr = s[0]
        size = 1
        counts = defaultdict(int)
        for i in range(1, len(s)):
            if s[i] != curr:
                add = 1
                while size > 0:
                    key = curr + str(size)
                    counts[key] += add
                    add += 1
                    size -= 1
                size = 1
                curr = s[i]
            else:
                size += 1
        add = 1
        # this checks for the last special substring (for example in "aabbba" we need to make sure the last 'a' is accounted for)
        while size > 0:
            key = curr + str(size)
            counts[key] += add
            add += 1
            size -= 1
        print(counts)

        # iterate through all of the recorded items and return the key that is both the largest and has a stored count of at least 3
        res = -1
        for key in counts:
            if counts[key] >= 3:
                res = max(res, int(key[1:]))
        return res
