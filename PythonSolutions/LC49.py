from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            counter[str(count)].append(s)
        return list(counter.values())


# use counters of the chars in the string to identify anagram words
