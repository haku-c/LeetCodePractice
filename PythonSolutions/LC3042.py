class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, index):
        current = self.root
        result = []
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            result.extend(current.end)
        current.end.append(index)
        return set(result)


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        prefs = Trie()
        suffs = Trie()
        for i in range(len(words)):
            word = words[i]
            pref = prefs.insert(word, i)
            suf = suffs.insert(word[::-1], i)
            res += len(pref.intersection(suf))
        return res
