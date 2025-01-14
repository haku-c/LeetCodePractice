from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wordsCounts = Counter()
        for word2 in words2:
            current = Counter(word2)
            for letter, counts in current.items():
                wordsCounts[letter] = max(wordsCounts[letter], counts)
        res = []
        for word in words1:
            current = Counter(word)
            match = True
            for letter, counts in wordsCounts.items():
                if counts > current[letter]:
                    match = False
                    break
            if match:
                res.append(word)
        return res
