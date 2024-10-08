# from collections import defaultdict


# this solution is a bit verbose and can be done with the counter library
# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         set1 = s1.split(" ")
#         set2 = s2.split(" ")
#         c1 = defaultdict(int)
#         c2 = defaultdict(int)
#         test = set(set1).union(set(set2))
#         for s in set1:
#             c1[s] += 1
#         for s in set2:
#             c2[s] += 1
#         res = []
#         for w in test:
#             if (c1[w] == 0 and c2[w] == 1) or (c1[w] == 1 and c2[w] == 0):
#                 res.append(w)
#         return res

from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(" ")
        words2 = s2.split(" ")
        counts1 = collections.Counter(words1)
        counts2 = collections.Counter(words2)
        res = []
        for word in counts1:
            if counts1[word] == 1 and counts2[word] == 0:
                res.append(word)
        for word in counts2:
            if counts2[word] == 1 and counts1[word] == 0:
                res.append(word)
        return res
