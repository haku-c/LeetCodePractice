from collections import Counter
from math import ceil


# using the counter is faster than the dictionary implementation
# the niche knowledge here is sorting in decreasing order using most_common()
# the default ordering is by the insertion order, which is not guaranteed to be decreasing by count
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        res = 0
        n = 1
        for _, number in c.most_common():
            res += number * ceil(n / 8)
            n += 1
        return res


# from collections import defaultdict
# from math import ceil
# class Solution:
#     def minimumPushes(self, word: str) -> int:
#         counts = defaultdict(int)
#         for c in word:
#             counts[c] += 1
#         pairs = sorted(counts.items(), key = lambda entry: entry[1], reverse = True)
#         res = 0
#         for i in range(len(pairs)):
#             number = pairs[i][1]
#             res += number * ceil((i+1)/8)
#         return res
